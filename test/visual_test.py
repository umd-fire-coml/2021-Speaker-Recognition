import unittest

from src.data_visualization_function import get_first


class VisualTest(unittest.TestCase):
    def test_load_data(self):
        self.assertEqual(get_first(), "LibriSpeech/train-clean-100/2518/154825/2518-154825-0045.flac")


if __name__ == '__main__':
    unittest.main()
