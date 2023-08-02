import random

import pandas as pd
import numpy as np
import os
import shutil
from datetime import datetime
import math
import gc
import copy


class IncrementalDataGenerator:
    def __init__(self,
                 datasetName: str = "PeMS07",
                 configFile: str = "config.json",
                 fullDynaFile: str = "PeMS07.dyna",
                 fullGeoFile: str = "PeMS07.geo",
                 fullRelFile: str = "PeMS07.rel",
                 outPutDir: str = os.path.join("..", r"raw_data\__PreProcessOutput\tmp"),
                 startSensorIdx: int = -1,
                 rdShuffleLength: int = -1,
                 timeBoundary: datetime = datetime.strptime("2023-07-01", "%Y-%m-%d"),
                 ):
        self.datasetName = datasetName
        self.configFile = configFile
        self.fullDynaFile: str = fullDynaFile
        self.fullGeoFile: str = fullGeoFile
        self.fullRelFile: str = fullRelFile
        self.outPutDir: str = outPutDir
        self.fullDyna: pd.DataFrame = pd.read_csv(self.fullDynaFile, index_col="dyna_id")
        self.fullGeo: pd.DataFrame = pd.read_csv(self.fullGeoFile, index_col="geo_id")
        self.fullRel: pd.DataFrame = pd.read_csv(self.fullRelFile, index_col="rel_id")
        self.startSensorIdx = startSensorIdx
        self.endSensorIdx = np.inf
        self.rdShuffleLength = rdShuffleLength
        self.timeBoundary: datetime = timeBoundary
        self.stage_1_workdir = os.path.join(self.outPutDir, r"stage1")
        self.stage_2_workdir = os.path.join(self.outPutDir, r"stage2")
        for _ in [self.outPutDir, self.stage_1_workdir, self.stage_2_workdir]:
            if not os.path.exists(_):
                os.makedirs(_)
        if self.startSensorIdx > 0:
            self.genNumOrderDataSet()
        else:
            if self.rdShuffleLength > 0:
                self.genSpatialTemporalSplitDataset()
            else:
                self.genTemporalSplitDataset()

    def genNumOrderDataSet(self):
        dyna = copy.deepcopy(self.fullDyna)
        dyna.drop(dyna[(dyna.entity_id < self.startSensorIdx) | (dyna.entity_id > self.endSensorIdx)].index,
                  inplace=True)
        dyna = dyna.reset_index()
        dyna["dyna_id"] = dyna.index
        dyna.to_csv(os.path.join(self.outPutDir, "dyna.csv"), index=False)
        geo = copy.deepcopy(self.fullGeo)
        # Should be as follows, while geo["geo_id"] as geo.index.
        geo.drop(geo[(geo.index < self.startSensorIdx) | (geo.index > self.endSensorIdx)].index, inplace=True)
        geo.to_csv(os.path.join(self.outPutDir, "geo.csv"), index=True)
        rel = copy.deepcopy(self.fullRel)
        rel.drop(rel[(rel.origin_id < self.startSensorIdx) | (rel.origin_id > self.endSensorIdx) |
                     (rel.destination_id < self.startSensorIdx) | (rel.destination_id > self.endSensorIdx)].index,
                 inplace=True)
        rel = rel.reset_index()
        rel["rel_id"] = rel.index
        rel.to_csv(os.path.join(self.outPutDir, "rel.csv"), index=False)
        del dyna, geo, rel
        gc.collect()

    def genSpatialTemporalSplitDataset(self):
        baseIndices = list(set(random.sample(range(len(self.fullGeo)), self.rdShuffleLength)))
        print(len(baseIndices), baseIndices)
        dyna_stage_1 = self.fullDyna.copy(deep=True)
        dyna_stage_2 = self.fullDyna.copy(deep=True)
        # Spatial shrink
        dyna_stage_1.drop([i for i, x in enumerate(zip(dyna_stage_1.entity_id, dyna_stage_1.time))
                           if (x[0] not in baseIndices) or
                           (datetime.strptime(x[1], "%Y-%m-%dT%H:%M:%SZ") > self.timeBoundary)], inplace=True)
        dyna_stage_2.drop([i for i, t in enumerate(dyna_stage_2.time) if
                           datetime.strptime(t, "%Y-%m-%dT%H:%M:%SZ") <= self.timeBoundary], inplace=True)
        # Reset Idx
        dyna_stage_1 = dyna_stage_1.reset_index()
        dyna_stage_1["dyna_id"] = dyna_stage_1.index
        dyna_stage_2 = dyna_stage_2.reset_index()
        dyna_stage_2["dyna_id"] = dyna_stage_2.index
        # Output
        dyna_stage_1.to_csv(os.path.join(self.stage_1_workdir, self.datasetName + ".dyna"), index=False)
        dyna_stage_2.to_csv(os.path.join(self.stage_2_workdir, self.datasetName + ".dyna"), index=False)
        geo_stage_1 = self.fullGeo.copy(deep=True)
        geo_stage_2 = self.fullGeo.copy(deep=True)
        # Should be as follows, while geo["geo_id"] as geo.index.
        geo_stage_1.drop([i for i, x in enumerate(geo_stage_1.index) if x not in baseIndices], inplace=True)
        geo_stage_1.to_csv(os.path.join(self.stage_1_workdir, self.datasetName + ".geo"), index=True)
        geo_stage_2.to_csv(os.path.join(self.stage_2_workdir, self.datasetName + ".geo"), index=True)
        rel_stage_1 = self.fullRel.copy(deep=True)
        rel_stage_2 = self.fullRel.copy(deep=True)
        rel_stage_1.drop([i for i, x in enumerate(zip(rel_stage_1.origin_id, rel_stage_1.destination_id)) if
                          (x[0] not in baseIndices) or (x[1] not in baseIndices)], inplace=True)
        rel_stage_1 = rel_stage_1.reset_index()
        rel_stage_1["rel_id"] = rel_stage_1.index
        rel_stage_1.to_csv(os.path.join(self.stage_1_workdir, self.datasetName + ".rel"), index=False)
        rel_stage_2.to_csv(os.path.join(self.stage_2_workdir, self.datasetName + ".rel"), index=False)
        # Copy config.json
        shutil.copy(self.configFile, os.path.join(self.stage_1_workdir, "config.json"))
        shutil.copy(self.configFile, os.path.join(self.stage_2_workdir, "config.json"))
        del dyna_stage_1, geo_stage_1, rel_stage_1, dyna_stage_2, geo_stage_2, rel_stage_2
        gc.collect()

    def genTemporalSplitDataset(self):
        dyna_stage_1 = self.fullDyna.copy(deep=True)
        dyna_stage_2 = self.fullDyna.copy(deep=True)
        # Temporal shrink 2017-05-01T00:00:00Z
        dyna_stage_1.drop([i for i, t in enumerate(dyna_stage_1.time) if
                           datetime.strptime(t, "%Y-%m-%dT%H:%M:%SZ") > self.timeBoundary], inplace=True)
        dyna_stage_2.drop([i for i, t in enumerate(dyna_stage_2.time) if
                           datetime.strptime(t, "%Y-%m-%dT%H:%M:%SZ") <= self.timeBoundary], inplace=True)
        # Reset Idx
        dyna_stage_1 = dyna_stage_1.reset_index()
        dyna_stage_1["dyna_id"] = dyna_stage_1.index
        dyna_stage_2 = dyna_stage_2.reset_index()
        dyna_stage_2["dyna_id"] = dyna_stage_2.index
        # Output
        dyna_stage_1.to_csv(os.path.join(self.stage_1_workdir, self.datasetName + ".dyna"), index=False)
        dyna_stage_2.to_csv(os.path.join(self.stage_2_workdir, self.datasetName + ".dyna"), index=False)
        # Geo and Reo are not modified.
        shutil.copy(self.fullGeoFile, self.stage_1_workdir)
        shutil.copy(self.fullGeoFile, self.stage_2_workdir)
        shutil.copy(self.fullRelFile, self.stage_1_workdir)
        shutil.copy(self.fullRelFile, self.stage_2_workdir)
        # Copy config.json
        shutil.copy(self.configFile, self.stage_1_workdir)
        shutil.copy(self.configFile, self.stage_1_workdir)
        del dyna_stage_1, dyna_stage_2
        gc.collect()
        return
