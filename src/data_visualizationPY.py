# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # Data Visualization
# 
# > In order to visualize the data, make sure that the data is downloaded and 
# the environment is set up correctly. 
# 
# 

# %%
import os
import librosa.display
import numpy as np
import random
import matplotlib.pyplot as plt
import IPython.display as ipd


# %%
def load_LibriSpeech_data():
    
    list_files_train = []
    speaker_id_train = []
    list_files_test = []
    speaker_id_test = []
    
    for speaker_name in os.listdir('LibriSpeech/train-clean-100/'):
        for chapter_name in os.listdir(os.path.join('LibriSpeech/train-clean-100/',
                                                    speaker_name)):
            for file_name in os.listdir(os.path.join('LibriSpeech/train-clean-100/',
                                              speaker_name +"/"+chapter_name)):
                if file_name.endswith('.flac'):
                    list_files_train.append(os.path.join('LibriSpeech/train-clean-100/',
                                  speaker_name +"/"+chapter_name+"/"+file_name))
                    speaker_id_train.append(file_name.split("-", 1)[0])

    for speaker_name in os.listdir('LibriSpeech/test-clean/'):
        for chapter_name in os.listdir(os.path.join('LibriSpeech/test-clean/',
                                                    speaker_name)):
            for file_name in os.listdir(os.path.join('LibriSpeech/test-clean/',
                                              speaker_name +"/"+chapter_name)):
                if file_name.endswith('.flac'):
                    list_files_test.append(os.path.join('LibriSpeech/test-clean/',
                                  speaker_name +"/"+chapter_name+"/"+file_name))
                    speaker_id_test.append(file_name.split("-", 1)[0])

    return list_files_train, speaker_id_train, list_files_test, speaker_id_test


files_train, speaker_id_train, files_test, speaker_id_test = load_LibriSpeech_data()

def get_first():
    s = "LibriSpeech/train-clean-100/2518/154825/2518-154825-0045.flac"
    return s


# %%
num_display = 3

audio_data_train = random.sample(files_train, num_display)
audio_data_test = random.sample(files_test, num_display)

print("Data being displayed: ")

print("Training data: ")
for i in audio_data_train:
  print(i)
  plt.figure(figsize=(15,4))
  plt.xlabel("Time", labelpad=-2)
  plt.title(i, pad=-1)
  data, sample_rate = librosa.load(i, sr=22050, mono=True, offset=0.0)
  librosa.display.waveplot(data, sr=sample_rate)
  ipd.display(ipd.Audio(data, rate=sample_rate))
print("Testing data: ")
for i in audio_data_test:
  print(i)
  plt.figure(figsize=(15,4))
  plt.xlabel("Time", labelpad=-2)
  plt.title(i, pad=-1)
  data, sample_rate = librosa.load(i, sr=22050, mono=True, offset=0.0)
  ipd.display(ipd.Audio(data, rate=sample_rate))
  librosa.display.waveplot(data, sr=sample_rate)


