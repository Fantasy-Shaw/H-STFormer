import os
from datetime import datetime
import pytz

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dateutil import parser


def draw_traffic_flow(nodes: list):
    time_boundary = datetime.strptime("2017-07-30", "%Y-%m-%d").replace(tzinfo=pytz.UTC)  # last 2 days
    dyna_file = os.path.join('../', 'raw_data/PeMS07/PeMS07.dyna')
    full_traffic_flow: pd.DataFrame = pd.read_csv(dyna_file)
    full_traffic_flow.drop(labels=['type'], axis=1)
    full_traffic_flow.drop([i for i, _ in enumerate(full_traffic_flow.entity_id) if _ not in nodes], inplace=True)
    full_traffic_flow = full_traffic_flow.reset_index()
    full_traffic_flow.drop([i for i, t in enumerate(full_traffic_flow.time) if parser.parse(t) < time_boundary],
                           inplace=True)
    full_traffic_flow = full_traffic_flow.reset_index()
    traffic_flow_map: dict = {}
    time_index = None
    for node in nodes:
        _traffic_flow = full_traffic_flow.copy(deep=True)
        _traffic_flow.drop([i for i, _ in enumerate(_traffic_flow.entity_id) if _ != node], inplace=True)
        if time_index is None:
            time_index = _traffic_flow['time']
        traffic_flow_map[node] = _traffic_flow['traffic_flow']
    print(traffic_flow_map)
    colors = ['#39c5bb', '#39c5bb', '#39c5bb', '#39c5bb']
    plt.figure(figsize=(15, 10))
    plt.rcParams['font.family'] = ['Times New Roman']
    plt.rcParams['font.size'] = 28
    for i, node in enumerate(nodes):
        plt.subplot(len(nodes) // 2, 2, i + 1)
        plt.ylim((0, 1100))
        plt.title('Node ' + str(node))
        plt.plot(time_index, traffic_flow_map[node], color=colors[i % len(colors)])
        plt.xticks([])
        plt.xticks(size=18)
    plt.savefig("sudden-events.jpg")


if __name__ == '__main__':
    draw_traffic_flow([114, 496, 567, 864])
    print("")
