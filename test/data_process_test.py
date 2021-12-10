import unittest
import pandas as pd
from src.data_Process import dataProcess

class MyTestCase(unittest.TestCase):
    def my_dataProcess(self):
        filePath = "data/cv-valid-train.csv"
        dataProcessor = dataProcess(filePath, ['text','up_votes','down_votes','age', 'accent', 'duration'], 5000, 20)
        return dataProcessor

    def test_create_and_drop(dataProcessor):
        dataProcessing = dataProcessor.my_dataProcess()
        dataProcessing.createDataframeAndDrop()
        columns = list(dataProcessing.dataHolder.columns)
        assert columns == ['filename', 'gender']

    def test_slice_and_trim(dataProcessor):
        dataProcessing = dataProcessor.my_dataProcess()
        dataProcessing.createDataframeAndDrop()
        dataProcessing.sliceAndTrim()
        assert dataProcessing.dataHolder.shape == (20, 2)

    def test_split(dataProcessor):
        dataProcessing = dataProcessor.my_dataProcess()
        dataProcessing.createDataframeAndDrop()
        dataProcessing.sliceAndTrim()
        test, train, valid = dataProcessing.splitTrainTestValid()
        assert test.shape == (2, 2)
        assert train.shape == (16, 2)
        assert valid.shape == (2, 2)


if __name__ == '__main__':
    unittest.main()
