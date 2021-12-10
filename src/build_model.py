from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Dropout
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping

class buildModel():

    def create_model(vector_length=40):
        model = Sequential()
        model.add(Dense(256, input_shape=(vector_length,)))
        model.add(Dropout(0.3))
        model.add(Dense(256, activation="relu"))
        model.add(Dropout(0.3))
        model.add(Dense(128, activation="relu"))
        model.add(Dropout(0.3))
        model.add(Dense(128, activation="relu"))
        model.add(Dropout(0.3))
        model.add(Dense(64, activation="relu"))
        model.add(Dropout(0.3))
        # one output neuron with sigmoid activation function, 0 means female, 1 means male
        model.add(Dense(1, activation="sigmoid"))
        # using binary crossentropy as it's male/female classification (binary)
        model.compile(loss="binary_crossentropy", metrics=["accuracy"], optimizer="adam")
        # print summary of the model
        model.summary()
        return model