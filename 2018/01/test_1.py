import unittest
from . import chronal_calibration_1


class TestChronalCalibration(unittest.TestCase):

    def test1(self):
        input = ["+1", "+1", "+1"]
        start_value = 0
        expected_result = 3
        actual_result = chronal_calibration_1.operate(input, start_value)
        self.assertEqual(expected_result, actual_result)

    def test2(self):
        input = ["+1", "+1", "-2"]
        start_value = 0
        expected_result = 0
        actual_result = chronal_calibration_1.operate(input, start_value)
        self.assertEqual(expected_result, actual_result)

    def test3(self):
        input = ["-1", "-2", "-3"]
        start_value = 0
        expected_result = -6
        actual_result = chronal_calibration_1.operate(input, start_value)
        self.assertEqual(expected_result, actual_result)


if __name__ == "__main__":
    unittest.main()
