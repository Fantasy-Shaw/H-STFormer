import torch
import torch.nn as nn
from logging import getLogger
import numpy as np
import math

from libcity.model.abstract_traffic_state_model import AbstractTrafficStateModel
from libcity.model import loss


def _gen_embedding(length, channels, min_timescale=1.0, max_timescale=1.0e4):
    position = np.arange(length)
    num_timescales = channels // 2
    log_timescale_increment = (math.log(float(max_timescale) / float(min_timescale)) / (float(num_timescales) - 1))
    inv_timescales = min_timescale * np.exp(np.arange(num_timescales).astype(np.float16) * -log_timescale_increment)
    scaled_time = np.expand_dims(position, 1) * np.expand_dims(inv_timescales, 0)

    signal = np.concatenate([np.sin(scaled_time), np.cos(scaled_time)], axis=1)
    signal = np.pad(signal, [[0, 0], [0, channels % 2]],
                    'constant', constant_values=[0.0, 0.0])
    signal = signal.reshape([1, length, channels])

    return torch.from_numpy(signal).type(torch.FloatTensor)


class MyFormer(AbstractTrafficStateModel):
    def __init__(self, config, data_feature):
        super().__init__(config, data_feature)

    def forward(self, x):
        pass


if __name__ == "__main__":
    # print(_gen_embedding(5, 5, 1, 50))
    data = np.array([[1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8]])
    data1 = data.reshape(4, 4)
    data2 = np.pad(data, [[2, 0], [0, 3]], 'constant')
    print(data2)
