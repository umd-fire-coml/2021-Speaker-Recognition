#import os.path
#import unittest
#from os import path

#def main(self):

   #print ("File exists:"+str(path.exists('src/download_script.py')))
 #  self.assertEquals("SpencerIsAwesome", "SpencerIsAwesome")

#if __name__== "__main__":
 #  main()


import os.path
import unittest
from os import path

class VisualTest(unittest.TestCase):
    def test_data_download(self):
        #self.assertEqual("SpencerIsAwesome", "SpencerIsAwesome")
        path.exists('src/download_script.py')


if __name__ == '__main__':
    unittest.main()