import unittest
from day1_1 import expense_report

class TestDay1_1(unittest.TestCase):
    def test_types(self):
        self.assertRaises(TypeError, expense_report, None)
        self.assertRaises(TypeError, expense_report, "test string")
        self.assertRaises(TypeError, expense_report, 1234)

    def test_input(self):
        oneVal = [1]
        self.assertRaises(AssertionError, expense_report, oneVal)

    def test_successful(self):
        twoValues = [1010, 1010]
        self.assertEqual(expense_report(twoValues), 1010*1010)
        basicData = [1721, 979, 366, 299, 675, 1456]
        self.assertEqual(expense_report(basicData), 514579)