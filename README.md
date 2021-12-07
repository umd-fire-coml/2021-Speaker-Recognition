# 2021 Speaker Recognition

### Product Description
--- 
The purpose of this project is to assess whether a given audio recording has a male or female speaker, which is decided through the recording's frequency. 

### Directory Guide
---

### Dataset
---
We used the [Common Voice dataset](https://www.kaggle.com/mozillaorg/common-voice) which is a dataset of speeches which is a collection of speech data that is gathered from various audio sources.
In particular, we used the cv-valid-train.csv and the cv-valid-train datasets. 

### Setting Up Your Environment
---
Import the following:
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
### Training the Model
---

### Testing the Model
---

### Citations and References
---
[1] Amidi , A., &amp; Amidi, S. (n.d.). A detailed example of how to use data generators with Keras. A detailed example of data generators with Keras. Retrieved December 7, 2021, from https://stanford.edu/~shervine/blog/keras-how-to-generate-data-on-the-fly. 
