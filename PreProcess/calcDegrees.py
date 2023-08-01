import pandas as pd
import numpy as np
import os
import math
import gc
import copy
import matplotlib.pyplot as plt
from brokenaxes import brokenaxes


class DegreeStatistics:
    def __init__(self):
        self.fullGeoFile: str = os.path.join("..", r"raw_data\PeMS07\PeMS07.geo")
        self.fullRelFile: str = os.path.join("..", r"raw_data\PeMS07\PeMS07.rel")
        self.nodeDegOutPut: str = os.path.join("..", r"raw_data\PeMS07\PeMS07_DegStat.csv")
        self.nodeDegStatOutPut: str = os.path.join("..", r"raw_data\PeMS07\PeMS07_DegStat2.csv")
        self.roadOutPut: str = os.path.join("..", r"raw_data\PeMS07\PeMS07_RoadStat.csv")
        self.nodeDegStatFigOutPut: str = os.path.join("..", r"raw_data\PeMS07\PeMS07_DegStat.jpg")
        self.roadFigOutPut: str = os.path.join("..", r"raw_data\PeMS07\PeMS07_RoadStat.jpg")
        self.fullGeo: pd.DataFrame = pd.read_csv(self.fullGeoFile, index_col="geo_id")
        self.fullRel: pd.DataFrame = pd.read_csv(self.fullRelFile, index_col="rel_id")
        # 入度
        self.posDegMap = dict(zip(self.fullGeo.index, [0] * len(self.fullGeo.index)))
        # 出度
        self.negDegMap = dict(zip(self.fullGeo.index, [0] * len(self.fullGeo.index)))
        self.degMap = dict(zip(self.fullGeo.index, [0] * len(self.fullGeo.index)))
        self.nodeDegs = None
        self.nodeDegStat = {}
        self.roadStatusStat = {}
        self.calc()

    def calc(self, vis=True):
        for src, dst in zip(self.fullRel.origin_id, self.fullRel.destination_id):
            self.posDegMap[src] += 1
            self.negDegMap[dst] += 1
            self.degMap[src] += 1
            self.degMap[dst] += 1
        self.nodeDegs = pd.concat([pd.DataFrame([self.degMap]), pd.DataFrame([self.posDegMap]),
                                   pd.DataFrame([self.negDegMap])], sort=False).T
        self.nodeDegs.columns = ['deg', 'pos_deg', 'neg_deg']
        self.nodeDegs.insert(self.nodeDegs.shape[1], 'geo_id', self.nodeDegs.index)
        self.nodeDegs = self.nodeDegs[['geo_id', 'deg', 'pos_deg', 'neg_deg']]
        self.nodeDegs.to_csv(self.nodeDegOutPut, index=False)
        for _, deg in zip(self.nodeDegs.geo_id, self.nodeDegs.deg):
            try:
                self.nodeDegStat[deg] += 1
            except KeyError:
                self.nodeDegStat[deg] = 1
        self.nodeDegStat = pd.DataFrame([self.nodeDegStat]).T
        self.nodeDegStat.columns = ['nums']
        self.nodeDegStat.insert(self.nodeDegStat.shape[1], 'degrees', self.nodeDegStat.index)
        self.nodeDegStat = self.nodeDegStat[['degrees', 'nums']]
        print(self.nodeDegStat)
        self.nodeDegStat.to_csv(self.nodeDegStatOutPut)
        for src, dst in zip(self.fullRel.origin_id, self.fullRel.destination_id):
            __w = self.nodeDegs.deg[src] + self.nodeDegs.deg[dst]
            try:
                self.roadStatusStat[__w] += 1
            except KeyError:
                self.roadStatusStat[__w] = 1
        self.roadStatusStat = pd.DataFrame([self.roadStatusStat]).T
        self.roadStatusStat.columns = ['nums']
        self.roadStatusStat.insert(self.roadStatusStat.shape[1], 'weight', self.roadStatusStat.index)
        self.roadStatusStat = self.roadStatusStat[['weight', 'nums']]
        self.roadStatusStat.to_csv(self.roadOutPut, index=False)
        # print(self.roadStatusStat)
        if vis:
            self.vis_edge()
            self.vis_node()

    def vis_edge(self):
        plt.figure()
        plt.rcParams['font.sans-serif'] = ['Times New Roman']
        plt.rcParams['axes.unicode_minus'] = False
        plt.rcParams['font.size'] = 18
        bax = brokenaxes(xlims=((0, 60), (730, 760)), despine=True)
        bax.set_title('Edges')
        bax.set_xlabel("Nums")
        bax.set_ylabel("Weights")
        bax.barh(self.roadStatusStat.weight, self.roadStatusStat.nums)
        for x, y in zip(self.roadStatusStat.weight, self.roadStatusStat.nums):
            bax.annotate(y, (y, x))
        plt.savefig(self.roadFigOutPut)
        plt.show()

    def vis_node(self):
        plt.figure()
        plt.rcParams['font.sans-serif'] = ['Times New Roman']
        plt.rcParams['axes.unicode_minus'] = False
        plt.rcParams['font.size'] = 18
        bax = brokenaxes(xlims=((0, 70), (780, 820)), despine=True)
        bax.set_title("Nodes")
        bax.set_xlabel("Nums")
        bax.set_ylabel("Degrees")
        bax.barh(self.nodeDegStat['degrees'], self.nodeDegStat['nums'], color='darkorange')
        for x, y in zip(self.nodeDegStat.degrees, self.nodeDegStat.nums):
            bax.annotate(y, (y, x))

        plt.savefig(self.nodeDegStatFigOutPut)
        # plt.show()


if __name__ == "__main__":
    DegreeStatistics()
