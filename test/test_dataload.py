from src.data_load import load_libre_data
import os

#if not os.path.exists("LibriSpeech"):
#    print("test extracting")
#    os.system("tar xzf train-clean-100.tar.gz")

def test_fail_and_then_success():
    assert(not load_libre_data("train-clean-100"))
#    assert(len(list(load_libre_data("LibriSpeech/train-clean-100/"))) == 28539)
