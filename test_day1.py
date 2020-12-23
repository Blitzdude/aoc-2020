import unittest
from day1 import expense_report, expense_report_advanced

class TestDay1_1(unittest.TestCase):
    def test_types(self):
        self.assertRaises(TypeError, expense_report, None)
        self.assertRaises(TypeError, expense_report, 1234)
        # Day 2 problem tests
        self.assertRaises(TypeError, expense_report_advanced, None)
        self.assertRaises(TypeError, expense_report_advanced, 1234)

    def test_input(self):
        oneVal = [1]
        self.assertRaises(AssertionError, expense_report, oneVal)
        self.assertRaises(AssertionError, expense_report_advanced, oneVal)
        twoValues =  [1010, 1010]
        self.assertRaises(AssertionError, expense_report_advanced, twoValues)

    def test_values(self):
        twoValues = [1010, 1010]
        self.assertEqual(expense_report(twoValues), 1010*1010)
        basicData = [1721, 979, 366, 299, 675, 1456]
        self.assertEqual(expense_report(basicData), 514579)
        self.assertEqual(expense_report_advanced(basicData), 241861950)