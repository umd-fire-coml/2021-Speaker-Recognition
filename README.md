# 2021 Speaker Recognition

### Product Description
--- 
The purpose of this project is to assess whether a given audio recording has a male or female speaker, which is decided through the recording's frequency. The application of this model can be used to decide if a user is male or female, this could enable call centers to know the gender of the speaker and with that information better sell their products. [This google colab notebook](https://colab.research.google.com/drive/1I_9aSYQpuDgT8flqihTSkah4qcZD37Ou?usp=sharing) contains all the code to run through the project.


### Model Architecture
---
The model architecture is a deep feedforward neural network. This means that it takes inputs and assigns weights, these are summed to create bias. With the inputs established the activation functions used to create the output of the neurons were relu functions. Although, the last was a sigmoid function to bring the value between one and zero. There are 6 dense layers in our deep feedforward neural network and they are all dense layers with some dropout. The loss function that is utilized is binary_crossentropy as a binary classification is occurring.

### Video Demonstration
---
[![Speaker Recognition](http://img.youtube.com/vi/tAmuJ8CYcvA/0.jpg)](http://www.youtube.com/watch?v=tAmuJ8CYcvA "2021 Speaker Recognition")
### Directory Guide
---
`requirements.txt` - has the import statements needed for the project
#### data
- `cv-valid-train.csv` - the file path labels are stored
#### src
- `build_model.py` - builds the deep feedforward neural network model to distinguish between male and female voices
- `data_Generator.py` - generates the input of the model to be used for training
- `data_Process.py` - cleans the data
- `model_checker.py` - tests the model on test data
- `model_training.py` - trains the model using the training set and validates using validation set
#### test 
- `build_model_test.py` - checks model has been properly built
- `data_generator_test.py` - checks the generated data
- `data_process_test.py` - ensures the methods within data_Process.py are functioning as expected
#### weights
- contains the weights

### Dataset
---
We used the [Common Voice dataset](https://www.kaggle.com/mozillaorg/common-voice) which is a dataset of speeches which is a collection of speech data that is gathered from various audio sources.
In particular, we used the cv valid train dataset which contains 195776 audio files. The cv-valid-train.csv contains a table that corresponds to the audio files in the cv valid train dataset, which includes the filename and gender. As for the gender, the files have been labeled as "male", "female", and "other". We cleaned the data by eliminating the "other" files, so that we would be able to have a simpler dataset to work with. 

![image](https://user-images.githubusercontent.com/89940944/145652329-a4f449e4-4283-41bc-9585-21a763f56487.png)

![image](https://user-images.githubusercontent.com/89940944/145652371-20e6f7a9-0513-405e-bff3-083ec0f110e7.png)

The model is able to discern which audio is male or female using the data shown here.

### Setting Up Your Environment
---
To download the data, you will need to have this repository in the "Colab/BigProjekt/" folder of your Google Drive. 
We used pandas, numpy, and librosa. The import statements used can be seen below:
```
import pandas as pd
import numpy as np
import os
import tqdm
import librosa
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Dropout
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping
from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import Sequence
import tensorflow as tf
```
### Downloading the Data
---
Download the cv-valid-train folder and the cv-valid-train.csv file into the folder of your Google Drive or environment and use the following lines to unzip the file by replacing with your file paths.

```
!unzip '/content/drive/MyDrive/Colab/data zips/cv-valid-train.csv.zip' -d '/content/drive/MyDrive/Colab/BigProjekt/'
!unzip '/content/drive/MyDrive/Colab/data zips/cv-valid-train.zip' -d '/content/'
```
### Training the Model
---
To train the model, the free GPU on google colab was utilized. The model callbacks that were defined and used were model checkpoints to save weights after each epoch and early stopping. The amount of epochs set to train or were one hundred with a batch size of 100. Data generators were used and passed into model fit for the data and labels. Training and validation data generators were used when fitting the model. In the google colab smaller data generators are also made if the computer being utilized is slow with training. This will allow you to train faster with a cut to the accuracy. If high accuracy is wanted, I would recommend training until timeout on google colab and then loading the weights and training again when the timout occurs.

### Testing the Model
---
Testing the model utilizes loops that iterate through batches, generated from the test data generator, and checks if the expected label matches the guess. This grabs the actual labels and uses predict to grab the result from the model. If the result is closer to zero then the guess is a female and if the result is closer to one then the guess is a female. In the loops the amount of correct guesses is tallied and is divided by the total number of guesses to return the accuracy.

### Citations and References
---
[1] A. Amidi and S. Amidi, ???A detailed example of how to use data generators with Keras,??? A detailed example of data generators with Keras. [Online]. Available: [https://stanford.edu/~shervine/blog/keras-how-to-generate-data-on-the-fly.](https://stanford.edu/~shervine/blog/keras-how-to-generate-data-on-the-fly) [Accessed: 07-Dec-2021]. 
[2] R. Bagheri, ???An introduction to Deep Feedforward Neural Networks,??? Medium, 28-Aug-2020. [Online]. Available: [https://towardsdatascience.com/an-introduction-to-deep-feedforward-neural-networks-1af281e306cd](https://towardsdatascience.com/an-introduction-to-deep-feedforward-neural-networks-1af281e306cd). [Accessed: 10-Dec-2021].
