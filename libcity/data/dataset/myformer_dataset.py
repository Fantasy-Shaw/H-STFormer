import gc
import os
import numpy as np
import pandas as pd
from fastdtw import fastdtw
from tqdm import tqdm
from libcity.data.dataset import TrafficStatePointDataset
from libcity.data.utils import generate_dataloader
from tslearn.clustering import TimeSeriesKMeans, KShape
from multiprocessing import Pool


def mp_dtw(objs):
    mp_data_mean = objs[0]
    mp_i = objs[1]
    j = objs[2]
    return fastdtw(mp_data_mean[:, mp_i, :], mp_data_mean[:, j, :], radius=6)


def mp_sh_mx(objs):
    sh_mx, i, j, k = objs[0], objs[1], objs[2], objs[3]
    return min(sh_mx[i, j], sh_mx[i, k] + sh_mx[k, j], 511)


class MyFormerDataset(TrafficStatePointDataset):

    def __init__(self, config):
        self.type_short_path = config.get('type_short_path', 'hop')
        super().__init__(config)
        self.cache_file_name = os.path.join('./libcity/cache/dataset_cache/',
                                            'MyFormer_point_based_{}.npz'.format(self.parameters_str))
        self.points_per_hour = 3600 // self.time_intervals
        self.dtw_matrix = self._get_dtw()
        self.points_per_day = 24 * 3600 // self.time_intervals
        self.cand_key_days = config.get("cand_key_days", 14)
        self.s_attn_size = config.get("s_attn_size", 3)
        self.n_cluster = config.get("n_cluster", 16)
        self.cluster_max_iter = config.get("cluster_max_iter", 5)
        self.cluster_method = config.get("cluster_method", "kshape")
        self.is_quick_debug_mode = config.get("is_quick_debug_mode", True)

        self.train_dataloader: object = None
        self.eval_dataloader: object = None
        self.test_dataloader: object = None

        self.mp_i = 0
        self.mp_data_mean: np.ndarray = np.ndarray(shape=[3, 3, 3])

    def _get_dtw(self):
        cache_path = './libcity/cache/dataset_cache/dtw_' + self.dataset + '.npy'
        # Multiprocessing
        pool = Pool()
        for ind, filename in enumerate(self.data_files):
            if ind == 0:
                df = self._load_dyna(filename)
            else:
                df = np.concatenate((df, self._load_dyna(filename)), axis=0)
        if not os.path.exists(cache_path):
            data_mean = np.mean(
                [df[24 * self.points_per_hour * i: 24 * self.points_per_hour * (i + 1)]
                 for i in range(df.shape[0] // (24 * self.points_per_hour))], axis=0)
            dtw_distance = np.zeros((self.num_nodes, self.num_nodes))
            for i in tqdm(range(self.num_nodes)):
                args = [(data_mean, i, j) for j in range(i, self.num_nodes)]
                _dtw_distance_dim2 = pool.map(mp_dtw, args)
                for j in range(i, self.num_nodes):
                    dtw_distance[i][j], _ = _dtw_distance_dim2[j - i]
                # [Deprecated] dtw with single process.
                # for j in range(i, self.num_nodes):
                #     dtw_distance[i][j], _ = fastdtw(data_mean[:, i, :], data_mean[:, j, :], radius=6)
            for i in range(self.num_nodes):
                for j in range(i):
                    dtw_distance[i][j] = dtw_distance[j][i]
            np.save(cache_path, dtw_distance)
        dtw_matrix = np.load(cache_path)
        self._logger.info('Load DTW matrix from {}'.format(cache_path))
        return dtw_matrix

    def _load_geo(self):
        geofile = pd.read_csv(self.data_path + self.geo_file + '.geo')
        self.geo_ids = list(geofile['geo_id'])
        self.num_nodes = len(self.geo_ids)
        self.geo_to_ind = {}
        for index, idx in enumerate(self.geo_ids):
            self.geo_to_ind[idx] = index
        self._logger.info("Loaded file " + self.geo_file + '.geo' + ', num_nodes=' + str(
            self.num_nodes) + ', len(self.geo_ids)=' + str(len(self.geo_ids)))

    def _load_rel(self):
        # pool = Pool()
        self.sd_mx = None
        super()._load_rel()
        self.raw_rel_dataframe = pd.read_csv(self.data_path + self.rel_file + '.rel')
        self._logger.info('Max adj_mx value = {}'.format(self.adj_mx.max()))
        self.sh_mx = self.adj_mx.copy()
        sh_mx_file = '{}.npy'.format(self.dataset)
        # If existed, won't calc again.
        if os.path.exists(sh_mx_file):
            self.sh_mx = np.load(sh_mx_file)
            self._logger.info('Loaded existing file {}.npy'.format(self.dataset))
            return
        # Calc for the first time
        if self.type_short_path == 'hop':
            self.sh_mx[self.sh_mx > 0] = 1
            self.sh_mx[self.sh_mx == 0] = 511
            for i in range(self.num_nodes):
                self.sh_mx[i, i] = 0
            for k in range(self.num_nodes):
                for i in range(self.num_nodes):
                    # Multiprocessing
                    # self.sh_mx[i] = np.array(
                    #     pool.map(min, [(self.sh_mx[i, j], self.sh_mx[i, k] + self.sh_mx[k, j], 511)
                    #                    for j in range(self.num_nodes)])
                    # )
                    # with single process.
                    for j in range(self.num_nodes):
                        self.sh_mx[i, j] = min(self.sh_mx[i, j], self.sh_mx[i, k] + self.sh_mx[k, j], 511)
            np.save(sh_mx_file, self.sh_mx)

    def _calculate_adjacency_matrix(self):
        # pool = Pool()
        self._logger.info("Start Calculate the weight by Gauss kernel!")
        self.sd_mx = self.adj_mx.copy()
        distances = self.adj_mx[~np.isinf(self.adj_mx)].flatten()
        std = distances.std()
        self.adj_mx = np.exp(-np.square(self.adj_mx / std))
        self.adj_mx[self.adj_mx < self.weight_adj_epsilon] = 0
        sd_mx_file = '{}_sd_mx.npy'.format(self.dataset)
        # If existed, won't calc again.
        if os.path.exists(sd_mx_file):
            self.sd_mx = np.load(sd_mx_file)
            self._logger.info('Loaded existing file {}_sd_mx.npy'.format(self.dataset))
            return
        # Calc for the first time
        if self.type_short_path == 'dist':
            self.sd_mx[self.adj_mx == 0] = np.inf
            for k in range(self.num_nodes):
                for i in range(self.num_nodes):
                    # Multiprocessing
                    # self.sd_mx[i] = np.array(
                    #     pool.map(min, [(self.sd_mx[i, j], self.sd_mx[i, k] + self.sd_mx[k, j])
                    #                    for j in range(self.num_nodes)])
                    # )
                    # with single process.
                    for j in range(self.num_nodes):
                        self.sd_mx[i, j] = min(self.sd_mx[i, j], self.sd_mx[i, k] + self.sd_mx[k, j])
            np.save(sd_mx_file, self.sd_mx)

    def get_data(self):
        x_train, y_train, x_val, y_val, x_test, y_test = [], [], [], [], [], []
        if self.data is None:
            self.data = {}
            if self.cache_dataset and os.path.exists(self.cache_file_name):
                x_train, y_train, x_val, y_val, x_test, y_test = self._load_cache_train_val_test()
            else:
                x_train, y_train, x_val, y_val, x_test, y_test = self._generate_train_val_test()
        self.feature_dim = x_train.shape[-1]
        self.ext_dim = self.feature_dim - self.output_dim
        self.scaler = self._get_scalar(self.scaler_type,
                                       x_train[..., :self.output_dim], y_train[..., :self.output_dim])
        self.ext_scaler = self._get_scalar(self.ext_scaler_type,
                                           x_train[..., self.output_dim:], y_train[..., self.output_dim:])
        x_train[..., :self.output_dim] = self.scaler.transform(x_train[..., :self.output_dim])
        y_train[..., :self.output_dim] = self.scaler.transform(y_train[..., :self.output_dim])
        x_val[..., :self.output_dim] = self.scaler.transform(x_val[..., :self.output_dim])
        y_val[..., :self.output_dim] = self.scaler.transform(y_val[..., :self.output_dim])
        x_test[..., :self.output_dim] = self.scaler.transform(x_test[..., :self.output_dim])
        y_test[..., :self.output_dim] = self.scaler.transform(y_test[..., :self.output_dim])
        if self.normal_external:
            x_train[..., self.output_dim:] = self.ext_scaler.transform(x_train[..., self.output_dim:])
            y_train[..., self.output_dim:] = self.ext_scaler.transform(y_train[..., self.output_dim:])
            x_val[..., self.output_dim:] = self.ext_scaler.transform(x_val[..., self.output_dim:])
            y_val[..., self.output_dim:] = self.ext_scaler.transform(y_val[..., self.output_dim:])
            x_test[..., self.output_dim:] = self.ext_scaler.transform(x_test[..., self.output_dim:])
            y_test[..., self.output_dim:] = self.ext_scaler.transform(y_test[..., self.output_dim:])
        if self.is_quick_debug_mode and self.dataset[0:4] == "PeMS":
            # For quickly debugging, don't calculate pattern key.
            self.pattern_key_file = os.path.join(
                './libcity/cache/dataset_cache/', 'pattern_keys_{}_{}_{}_{}_{}_{}'.format(
                    self.cluster_method, self.dataset[0:6], self.cand_key_days, self.s_attn_size, self.n_cluster,
                    self.cluster_max_iter))
            self._logger.info("Using quick-debug-mode, won't calculate clustering pattern key.")
        else:
            self.pattern_key_file = os.path.join(
                './libcity/cache/dataset_cache/', 'pattern_keys_{}_{}_{}_{}_{}_{}'.format(
                    self.cluster_method, self.dataset, self.cand_key_days, self.s_attn_size, self.n_cluster,
                    self.cluster_max_iter))
        if not os.path.exists(self.pattern_key_file + '.npy'):
            cand_key_time_steps = self.cand_key_days * self.points_per_day
            pattern_cand_keys = (x_train[:cand_key_time_steps, :self.s_attn_size, :, :self.output_dim]
                                 .swapaxes(1, 2).reshape(-1, self.s_attn_size, self.output_dim))
            self._logger.info("Clustering...")
            if self.cluster_method == "kshape":
                km = KShape(n_clusters=self.n_cluster, max_iter=self.cluster_max_iter).fit(pattern_cand_keys)
            else:
                km = TimeSeriesKMeans(n_clusters=self.n_cluster, metric="softdtw", max_iter=self.cluster_max_iter).fit(
                    pattern_cand_keys)
            self.pattern_keys = km.cluster_centers_
            np.save(self.pattern_key_file, self.pattern_keys)
            self._logger.info("Saved at file " + self.pattern_key_file + ".npy")
        else:
            self.pattern_keys = np.load(self.pattern_key_file + ".npy")
            self._logger.info("Loaded file " + self.pattern_key_file + ".npy")
        train_data = list(zip(x_train, y_train))
        del x_train, y_train
        gc.collect()
        eval_data = list(zip(x_val, y_val))
        del x_val, y_val
        gc.collect()
        test_data = list(zip(x_test, y_test))
        del x_test, y_test
        gc.collect()
        self.train_dataloader, self.eval_dataloader, self.test_dataloader = \
            generate_dataloader(train_data, eval_data, test_data, self.feature_name,
                                self.batch_size, self.num_workers, pad_with_last_sample=self.pad_with_last_sample,
                                distributed=self.distributed)
        self.num_batches = len(self.train_dataloader)
        return self.train_dataloader, self.eval_dataloader, self.test_dataloader

    def get_data_feature(self):
        return {"scaler": self.scaler, "adj_mx": self.adj_mx, "sd_mx": self.sd_mx, "sh_mx": self.sh_mx,
                "ext_dim": self.ext_dim, "num_nodes": self.num_nodes, "feature_dim": self.feature_dim,
                "output_dim": self.output_dim, "num_batches": self.num_batches,
                "dtw_matrix": self.dtw_matrix, "pattern_keys": self.pattern_keys,
                "raw_rel_dataframe": self.raw_rel_dataframe}
