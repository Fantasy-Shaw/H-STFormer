import random

import pandas as pd
import numpy as np
import os
from datetime import datetime
import math
import gc
import copy


class IncrementalDataGenerator:
    def __init__(self,
                 fullDynaFile: str = os.path.join("..", r"raw_data\PeMS07\PeMS07.dyna"),
                 fullGeoFile: str = os.path.join("..", r"raw_data\PeMS07\PeMS07.geo"),
                 fullRelFile: str = os.path.join("..", r"raw_data\PeMS07\PeMS07.rel"),
                 outPutDir: str = os.path.join("..", r"raw_data\__PreProcessOutput\PeMS07LiteTest"),
                 startSensorIdx: int = -1,
                 rdShuffleLength: int = 320,
                 timeBoundary: datetime = datetime.strptime("2023-07-01", "%Y-%m-%d").date(),
                 ):
        self.fullDynaFile: str = fullDynaFile
        self.fullGeoFile: str = fullGeoFile
        self.fullRelFile: str = fullRelFile
        self.outPutDir: str = outPutDir
        self.fullDyna: pd.DataFrame = pd.read_csv(self.fullDynaFile, index_col="dyna_id")
        self.fullGeo: pd.DataFrame = pd.read_csv(self.fullGeoFile, index_col="geo_id")
        self.fullRel: pd.DataFrame = pd.read_csv(self.fullRelFile, index_col="rel_id")
        self.startSensorIdx = 571
        self.endSensorIdx = np.inf
        self.rdShuffleLength = 320
        self.timeBoundary: datetime = timeBoundary
        if startSensorIdx > 0:
            self.startSensorIdx = startSensorIdx
            self.genNumOrderDataSet()
        else:
            self.rdShuffleLength = rdShuffleLength
            self.genRandomShuffledDataset()

    def genNumOrderDataSet(self):
        if not os.path.exists(self.outPutDir):
            os.makedirs(self.outPutDir)
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

    def genRandomShuffledDataset(self):
        if not os.path.exists(self.outPutDir):
            os.makedirs(self.outPutDir)
        baseIndices = list(set(random.sample(range(len(self.fullGeo)), self.rdShuffleLength)))
        print(len(baseIndices), baseIndices)
        dyna_stage_1 = copy.deepcopy(self.fullDyna)
        dyna_stage_1.drop([i for i, x in enumerate(dyna_stage_1.entity_id) if x not in baseIndices], inplace=True)
        dyna_stage_1 = dyna_stage_1.reset_index()
        dyna_stage_1["dyna_id"] = dyna_stage_1.index
        dyna_stage_1.to_csv(os.path.join(self.outPutDir, "dyna.csv"), index=False)
        geo_stage_1 = copy.deepcopy(self.fullGeo)
        # Should be as follows, while geo["geo_id"] as geo.index.
        geo_stage_1.drop([i for i, x in enumerate(geo_stage_1.index) if x not in baseIndices], inplace=True)
        geo_stage_1.to_csv(os.path.join(self.outPutDir, "geo.csv"), index=True)
        rel_stage_1 = copy.deepcopy(self.fullRel)
        rel_stage_1.drop([i for i, x in enumerate(zip(rel_stage_1.origin_id, rel_stage_1.destination_id)) if
                          (x[0] not in baseIndices) or (x[1] not in baseIndices)], inplace=True)
        rel_stage_1 = rel_stage_1.reset_index()
        rel_stage_1["rel_id"] = rel_stage_1.index
        rel_stage_1.to_csv(os.path.join(self.outPutDir, "rel.csv"), index=False)
        del dyna_stage_1, geo_stage_1, rel_stage_1
        gc.collect()


if __name__ == "__main__":
    IncrementalDataGenerator()
