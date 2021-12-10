import pandas as pd
import numpy as np
import librosa
from tensorflow.keras.layers import Dense, LSTM, Dropout
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping
from tensorflow.keras.utils import Sequence
from tensorflow.keras.models import Sequential
from src.build_model import buildModel
from src.data_Process import dataProcess

class actual_training():
    filePath = "C:/Users/potte/2021-Speaker-Recognition/ThingsNeeded/cv-valid-train.csv"
    dataProcessor = dataProcess(filePath, ['text', 'up_votes', 'down_votes', 'age', 'accent', 'duration'], 5000, 20)

    dataProcessing = dataProcessor.my_dataProcess()
    dataProcessing.createDataframeAndDrop()
    dataProcessing.sliceAndTrim()
    test, train, validate = dataProcessing.splitTrainTestValid()

    model = buildModel.create_model(vector_length=40)
    # define modelCheckpoint
    model_checkpoint = ModelCheckpoint(
        filepath='/content/drive/MyDrive/Colab/BigProjekt/weight/chkpoint/epoch{epoch:03d}_loss{loss:.3f}.hdf5',
        verbose=1, save_best_only=False, mode='min', save_weights_only='true')
    # define early stopping to stop training after 5 epochs of not improving
    early_stopping = EarlyStopping(mode="min", patience=5, restore_best_weights=True)

    epochs = 100
    # train the model using the training set and validating using validation set
    model.fit(x=train, epochs=epochs, validation_data=validate,
              callbacks=[model_checkpoint, early_stopping])

