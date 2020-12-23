import unittest
from common import read_file_to_list
from math import pi

class testCircleArea(unittest.TestCase):
    def test_input(self):
        self.assertRaises(TypeError, read_file_to_list, None)
        self.assertRaises(FileNotFoundError, read_file_to_list, "notfound.txt")
        
    def test_returns(self):
        self.assertIsInstance(read_file_to_list("input/test_input.txt"), list)
        pass