import librosa
import numpy as np
from tensorflow.keras.utils import Sequence



class DataGenerator(Sequence):

    def __init__(self, batch_size, dataset, n_mfccs):
        self.batch_size = batch_size
        self.dataset = dataset
        self.n_mfccs = n_mfccs
        self.on_epoch_end()


    def __len__(self):
        """Denotes the number of batches per epoch
        :return: number of batches per epoch
        """
        return int(np.floor(len(self.dataset) / self.batch_size))

    def __getitem__(self, index):
        """Generate one batch of data
        :param index: index of the batch
        :return: x_batch and y_batch
        """
        # Initialization
        x_batch = np.empty((self.batch_size, self.n_mfccs))
        y_batch = np.empty((self.batch_size, 1))

        # Generate indexes of the batch
        indexes = self.indexes[index * self.batch_size : (index + 1) * self.batch_size]
        pos_in_array = 0
        # Generate data
        for i in indexes:
            x_batch[pos_in_array,] = self.generate_x(self.dataset.iloc[i][0])
            y_batch[pos_in_array,] = self.generate_y(self.dataset.iloc[i][1])
            pos_in_array += 1

        # Return batch data
        return x_batch, y_batch



    def on_epoch_end(self):
        """Shuffle indexes after each epoch
        """
        self.indexes = np.arange(len(self.dataset))
        np.random.shuffle(self.indexes)

    def generate_x(self, data_path):
        x, sr = librosa.load(data_path)
        mfccs = np.mean(librosa.feature.mfcc(y=x, sr=sr, n_mfcc=40).T, axis=0)
        return mfccs


    def generate_y(self, gender):
        label_to_int = {'male' : 1, 'female' : 0}
        return label_to_int[gender]