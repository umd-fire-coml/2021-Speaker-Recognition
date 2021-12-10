from src.data_Generator import DataGenerator
from src.data_Process import dataProcess
from src.build_model import buildModel
import pandas as pd
import numpy as np
import librosa
from tensorflow.keras.layers import Dense, LSTM, Dropout
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping
from tensorflow.keras.utils import Sequence
from tensorflow.keras.models import Sequential

class modelChecker():

    def foo(self):
        filePath = "C:/Users/potte/2021-Speaker-Recognition/ThingsNeeded/cv-valid-train.csv"
        dataProcessor = dataProcess(filePath, ['text', 'up_votes', 'down_votes', 'age', 'accent', 'duration'], 5000, 20)

        dataProcessing = dataProcessor.my_dataProcess()
        dataProcessing.createDataframeAndDrop()
        dataProcessing.sliceAndTrim()
        test, train, valid = dataProcessing.splitTrainTestValid()

        double_to_label = {1.0: 'male', 0.0: 'female'}
        model = buildModel.create_model(vector_length=40)
        model.load_weights('C:/Users/potte/PycharmProjects/pythonProject1/things/epoch001_loss2.033.hdf5')
        batchNum = 0
        totalGuess = 0
        guessCorrect = 0

        while (batchNum <= 3):
            index = 0
            feature, label = test[batchNum]
            for i in feature:

                guess = 0.5
                print("actual:")
                print(double_to_label[list(label[index])[0]])
                testFeature = i.reshape(1, -1)
                result = model.predict(x=testFeature)
                print("modelThing: %f", result)
                if (result < .5):
                    guess = 0.0
                    print('guess: female')
                else:
                    guess = 1.0
                    print('guess: male')
                if (guess == list(label[index])[0]):
                    guessCorrect += 1
                totalGuess += 1
                index += 1
                print(totalGuess)
                print(guessCorrect)
            batchNum += 1
        print(guessCorrect/totalGuess)
        return guessCorrect/totalGuess
