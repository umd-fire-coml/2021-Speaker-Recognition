import pandas as pd
import numpy as np
import math

class dataProcess():

    """pathToCsv is a string that holds the path to the csv, columnsToDrop is an array of strings,
       sliceLength is an int that slices the dataframe, numSamples holds the amount of samples desired"""
    def __init__(self, pathToCsv, columnsToDrop, sliceLength, numSamples):
        self.pathToCsv = pathToCsv
        self.columnsToDrop = columnsToDrop
        self.sliceLength = sliceLength
        self.numSamples = numSamples
        self.dataHolder = None

    """This creates the dataframe using the pathToCsv and the columnsToDrop"""
    def createDataframeAndDrop(self):
        self.dataHolder = pd.read_csv(self.pathToCsv)

        for column in self.columnsToDrop:
            if column in self.dataHolder.columns:
                self.dataHolder = self.dataHolder.drop([column], axis=1)

    """This trims the dataframe and slices it. Also gets rid of the N/A and other rows"""
    def sliceAndTrim(self):
        self.dataHolder = self.dataHolder[:self.sliceLength]

        for row in self.dataHolder.itertuples(True, None):
            if (pd.isnull(row[2]) or row[2] == 'other'):
                self.dataHolder = self.dataHolder.drop([row[0]])

        if (self.numSamples%2 != 0):
            self.numSamples += 1

        numMaleSamples = 0
        numFemaleSamples = 0
        for row in self.dataHolder.itertuples(True, None):
            if (row[2] == 'male' and numMaleSamples >= (self.numSamples / 2)):
                self.dataHolder = self.dataHolder.drop(row[0])
            if (row[2] == 'male' and numMaleSamples <= (self.numSamples / 2)):
                numMaleSamples += 1
            if (row[2] == 'female' and numFemaleSamples >= (self.numSamples / 2)):
                self.dataHolder = self.dataHolder.drop(row[0])
            if (row[2] == 'female' and numFemaleSamples <= (self.numSamples / 2)):
                numFemaleSamples += 1

    """Uses a split of 80 percent for training and 10 for training and testing"""
    def splitTrainTestValid(self):
        test = pd.DataFrame(columns=['filename', 'gender'])
        train = pd.DataFrame(columns=['filename', 'gender'])
        valid = pd.DataFrame(columns=['filename', 'gender'])

        mStest = 0; fStest = 0; mSvalid = 0; fSvalid = 0

        tenPercent = math.floor(self.numSamples * .1)
        if (tenPercent%2 != 0):
            tenPercent += 1

        for row in self.dataHolder.itertuples(False, None):
            if (row[1] == 'male' and mStest < (tenPercent / 2)):
                test.loc[len(test)] = row
                mStest += 1
            elif (row[1] == 'female' and fStest < (tenPercent / 2)):
                test.loc[len(test)] = row
                fStest += 1
            elif (row[1] == 'male' and mSvalid < (tenPercent / 2)):
                valid.loc[len(valid)] = row
                mSvalid += 1
            elif (row[1] == 'female' and fSvalid < (tenPercent / 2)):
                valid.loc[len(valid)] = row
                fSvalid += 1
            else:
                train.loc[len(train)] = row

        return test, train, valid
