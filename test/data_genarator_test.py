import unittest
from src.data_Generator import DataGenerator
from src.data_Process import dataProcess
import audioread
import scipy
import scikit-learn
import joblib
import decorator
import six
import resampy
import numba
import soundfile
import librosa
import numpy as np

class MyTestCase(unittest.TestCase):
    def my_data_generator(self):
        filePath = "data/cv-valid-train.csv"
        dataProcessor = dataProcess(filePath, ['text', 'up_votes', 'down_votes', 'age', 'accent', 'duration'], 5000, 20)
        dataProcessing = dataProcessor.my_dataProcess()
        dataProcessing.createDataframeAndDrop()
        dataProcessing.sliceAndTrim()
        dataGen = DataGenerator(batch_size=8, dataset=dataProcessing.dataHolder, n_mfccs=40)
        return dataGen

    def test_batch_size(dataGen):
        data_gen = dataGen.my_data_generator()
        assert len(data_gen.__getitem__(1)[0]) == data_gen.batch_size

    def test_generate_x(dataGen):
        data_gen = dataGen.my_data_generator()
        gen_mfcc = data_gen.generate_x(data_gen.dataset.iloc[0][0])
        x, sr = librosa.load(data_gen.dataset.iloc[0][0])
        exp_mfccs = np.mean(librosa.feature.mfcc(y=x, sr=sr, n_mfcc=40).T, axis=0)
        assert gen_mfcc == exp_mfccs

    def test_generate_y(dataGen):
        data_gen = dataGen.my_data_generator()
        assert data_gen.generate_y('female') == 0
        assert data_gen.generate_y('male') == 1

if __name__ == '__main__':
    unittest.main()
