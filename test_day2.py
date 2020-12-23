import unittest
from day2 import passwordConfirmation

class TestDay1_1(unittest.TestCase):

    def setUp(self):
        self.validPassword = ["1-3 a: abcde"]
        self.invalidPassword = ["1-3 b: cdefg"]

    def test_types(self):
        self.assertRaises(AssertionError, passwordConfirmation, None)
        self.assertRaises(TypeError, passwordConfirmation, 1234)
    def test_input(self):
        self.assertEqual(passwordConfirmation(self.validPassword), 1)
        self.assertEqual(passwordConfirmation(self.invalidPassword), 0)