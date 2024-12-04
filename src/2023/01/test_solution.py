#!/usr/bin/env python

import unittest
from . import solution


class TestSolution(unittest.TestCase):
    def test_1(self):
        calibration_data = solution.parse_input_file("test_input.txt")
        test_result = solution.sum_calibration_values(calibration_data)
        self.assertEqual(test_result, 142)

    def test_2(self):
        calibration_data = solution.parse_input_file("test_input2.txt")
        test_result = solution.sum_advanced_calibration_values(calibration_data)
        self.assertEqual(test_result, 281)


if __name__ == "__main__":
    unittest.main()
