import unittest
from src.build_model import buildModel
from tensorflow.keras.models import Model

class MyTestCase(unittest.TestCase):
    def my_model(self):
        actualModel = buildModel.create_model(vector_length=40)
        return actualModel

    def test_model_is_model_instance(my_model):
        actual_model = my_model.my_model()
        assert isinstance(actual_model, Model)


if __name__ == '__main__':
    unittest.main()
