# 2021 Speaker Recognition

### Product Description
--- 
The purpose of this project is to assess whether a given audio recording has a male or female speaker, which is decided through the recording's frequency. 

### Model Architecture
---

### Video Demonstration
---

### Directory Guide
---

### Dataset
---
We used the [Common Voice dataset](https://www.kaggle.com/mozillaorg/common-voice) which is a dataset of speeches which is a collection of speech data that is gathered from various audio sources.
In particular, we used the cv valid train dataset which contains 195776 audio files. The cv-valid-train.csv contains a table that corresponds to the audio files in the cv valid train dataset, which includes the filename and gender. As for the gender, the files have been labeled as "male", "female", and "other". We cleaned the data by eliminating the "other" files, so that we would be able to have a simpler dataset to work with. 

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
We downloaded the cv-valid-train folder and the cv-valid-train.csv file into the "Colab/BigProjekt/" folder of your Google Drive and use the following lines to unzip the file.

```
!unzip '/content/drive/MyDrive/Colab/data zips/cv-valid-train.csv.zip' -d '/content/drive/MyDrive/Colab/BigProjekt/'
!unzip '/content/drive/MyDrive/Colab/data zips/cv-valid-train.zip' -d '/content/'
```
### Training the Model
---

### Testing the Model
---

### Citations and References
---
[1] A. Amidi and S. Amidi, “A detailed example of how to use data generators with Keras,” A detailed example of data generators with Keras. [Online]. Available: [https://stanford.edu/~shervine/blog/keras-how-to-generate-data-on-the-fly.](https://stanford.edu/~shervine/blog/keras-how-to-generate-data-on-the-fly) [Accessed: 07-Dec-2021]. 
