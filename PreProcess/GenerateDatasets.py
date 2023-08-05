import _thread
import gc
from datetime import datetime
import os

from PreProcess.DatasetGenerator import IncrementalDataGenerator


def genPeMS03():
    # Unavailable
    return


def genPeMS04():
    IncrementalDataGenerator(
        datasetName="PeMS04",
        configFile=os.path.join("..", r"raw_data\PeMS04\config.json"),
        fullDynaFile=os.path.join("..", r"raw_data\PeMS04\PeMS04.dyna"),
        fullGeoFile=os.path.join("..", r"raw_data\PeMS04\PeMS04.geo"),
        fullRelFile=os.path.join("..", r"raw_data\PeMS04\PeMS04.rel"),
        outPutDirPrefix=os.path.join("..", r"raw_data\__PreProcessOutput\PeMS04ST60"),
        rdShuffleLength=184,
        timeBoundary=datetime.strptime("2018-02-04", "%Y-%m-%d"),
    )
    IncrementalDataGenerator(
        datasetName="PeMS04",
        configFile=os.path.join("..", r"raw_data\PeMS04\config.json"),
        fullDynaFile=os.path.join("..", r"raw_data\PeMS04\PeMS04.dyna"),
        fullGeoFile=os.path.join("..", r"raw_data\PeMS04\PeMS04.geo"),
        fullRelFile=os.path.join("..", r"raw_data\PeMS04\PeMS04.rel"),
        outPutDirPrefix=os.path.join("..", r"raw_data\__PreProcessOutput\PeMS04ST80"),
        rdShuffleLength=246,
        timeBoundary=datetime.strptime("2018-02-15", "%Y-%m-%d"),
    )
    IncrementalDataGenerator(
        datasetName="PeMS04",
        configFile=os.path.join("..", r"raw_data\PeMS04\config.json"),
        fullDynaFile=os.path.join("..", r"raw_data\PeMS04\PeMS04.dyna"),
        fullGeoFile=os.path.join("..", r"raw_data\PeMS04\PeMS04.geo"),
        fullRelFile=os.path.join("..", r"raw_data\PeMS04\PeMS04.rel"),
        outPutDirPrefix=os.path.join("..", r"raw_data\__PreProcessOutput\PeMS04T60"),
        timeBoundary=datetime.strptime("2018-02-04", "%Y-%m-%d"),
    )
    IncrementalDataGenerator(
        datasetName="PeMS04",
        configFile=os.path.join("..", r"raw_data\PeMS04\config.json"),
        fullDynaFile=os.path.join("..", r"raw_data\PeMS04\PeMS04.dyna"),
        fullGeoFile=os.path.join("..", r"raw_data\PeMS04\PeMS04.geo"),
        fullRelFile=os.path.join("..", r"raw_data\PeMS04\PeMS04.rel"),
        outPutDirPrefix=os.path.join("..", r"raw_data\__PreProcessOutput\PeMS04T80"),
        timeBoundary=datetime.strptime("2018-02-15", "%Y-%m-%d"),
    )
    return


def genPeMS07():
    IncrementalDataGenerator(
        datasetName="PeMS07",
        configFile=os.path.join("..", r"raw_data\PeMS07\config.json"),
        fullDynaFile=os.path.join("..", r"raw_data\PeMS07\PeMS07.dyna"),
        fullGeoFile=os.path.join("..", r"raw_data\PeMS07\PeMS07.geo"),
        fullRelFile=os.path.join("..", r"raw_data\PeMS07\PeMS07.rel"),
        outPutDirPrefix=os.path.join("..", r"raw_data\__PreProcessOutput\PeMS07ST60"),
        rdShuffleLength=530,
        timeBoundary=datetime.strptime("2017-06-25", "%Y-%m-%d"),
    )
    IncrementalDataGenerator(
        datasetName="PeMS07",
        configFile=os.path.join("..", r"raw_data\PeMS07\config.json"),
        fullDynaFile=os.path.join("..", r"raw_data\PeMS07\PeMS07.dyna"),
        fullGeoFile=os.path.join("..", r"raw_data\PeMS07\PeMS07.geo"),
        fullRelFile=os.path.join("..", r"raw_data\PeMS07\PeMS07.rel"),
        outPutDirPrefix=os.path.join("..", r"raw_data\__PreProcessOutput\PeMS07ST80"),
        rdShuffleLength=706,
        timeBoundary=datetime.strptime("2017-07-13", "%Y-%m-%d"),
    )
    IncrementalDataGenerator(
        datasetName="PeMS07",
        configFile=os.path.join("..", r"raw_data\PeMS07\config.json"),
        fullDynaFile=os.path.join("..", r"raw_data\PeMS07\PeMS07.dyna"),
        fullGeoFile=os.path.join("..", r"raw_data\PeMS07\PeMS07.geo"),
        fullRelFile=os.path.join("..", r"raw_data\PeMS07\PeMS07.rel"),
        outPutDirPrefix=os.path.join("..", r"raw_data\__PreProcessOutput\PeMS07T60"),
        timeBoundary=datetime.strptime("2017-06-25", "%Y-%m-%d"),
    )
    IncrementalDataGenerator(
        datasetName="PeMS07",
        configFile=os.path.join("..", r"raw_data\PeMS07\config.json"),
        fullDynaFile=os.path.join("..", r"raw_data\PeMS07\PeMS07.dyna"),
        fullGeoFile=os.path.join("..", r"raw_data\PeMS07\PeMS07.geo"),
        fullRelFile=os.path.join("..", r"raw_data\PeMS07\PeMS07.rel"),
        outPutDirPrefix=os.path.join("..", r"raw_data\__PreProcessOutput\PeMS07T80"),
        timeBoundary=datetime.strptime("2017-07-13", "%Y-%m-%d"),
    )
    return


def genPeMS08():
    IncrementalDataGenerator(
        datasetName="PeMS08",
        configFile=os.path.join("..", r"raw_data\PeMS08\config.json"),
        fullDynaFile=os.path.join("..", r"raw_data\PeMS08\PeMS08.dyna"),
        fullGeoFile=os.path.join("..", r"raw_data\PeMS08\PeMS08.geo"),
        fullRelFile=os.path.join("..", r"raw_data\PeMS08\PeMS08.rel"),
        outPutDirPrefix=os.path.join("..", r"raw_data\__PreProcessOutput\PeMS08ST60"),
        rdShuffleLength=102,
        timeBoundary=datetime.strptime("2016-08-06", "%Y-%m-%d"),
    )
    IncrementalDataGenerator(
        datasetName="PeMS08",
        configFile=os.path.join("..", r"raw_data\PeMS08\config.json"),
        fullDynaFile=os.path.join("..", r"raw_data\PeMS08\PeMS08.dyna"),
        fullGeoFile=os.path.join("..", r"raw_data\PeMS08\PeMS08.geo"),
        fullRelFile=os.path.join("..", r"raw_data\PeMS08\PeMS08.rel"),
        outPutDirPrefix=os.path.join("..", r"raw_data\__PreProcessOutput\PeMS08ST80"),
        rdShuffleLength=136,
        timeBoundary=datetime.strptime("2016-08-18", "%Y-%m-%d"),
    )
    IncrementalDataGenerator(
        datasetName="PeMS08",
        configFile=os.path.join("..", r"raw_data\PeMS08\config.json"),
        fullDynaFile=os.path.join("..", r"raw_data\PeMS08\PeMS08.dyna"),
        fullGeoFile=os.path.join("..", r"raw_data\PeMS08\PeMS08.geo"),
        fullRelFile=os.path.join("..", r"raw_data\PeMS08\PeMS08.rel"),
        outPutDirPrefix=os.path.join("..", r"raw_data\__PreProcessOutput\PeMS08T60"),
        timeBoundary=datetime.strptime("2016-08-06", "%Y-%m-%d"),
    )
    IncrementalDataGenerator(
        datasetName="PeMS08",
        configFile=os.path.join("..", r"raw_data\PeMS08\config.json"),
        fullDynaFile=os.path.join("..", r"raw_data\PeMS08\PeMS08.dyna"),
        fullGeoFile=os.path.join("..", r"raw_data\PeMS08\PeMS08.geo"),
        fullRelFile=os.path.join("..", r"raw_data\PeMS08\PeMS08.rel"),
        outPutDirPrefix=os.path.join("..", r"raw_data\__PreProcessOutput\PeMS08T80"),
        timeBoundary=datetime.strptime("2016-08-18", "%Y-%m-%d"),
    )
    return


if __name__ == "__main__":
    genPeMS03()
    genPeMS04()
    genPeMS07()
    genPeMS08()
