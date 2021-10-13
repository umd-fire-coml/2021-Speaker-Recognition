import os.path
import unittest
from os import path

class VisualTest(unittest.TestCase):
   def test_data_download(self):
      path.exists('src/requirements.txt')

if __name__== "__main__":
   unittest.main()
