import unittest
from . import chronal_calibration_2


class TestChronalCalibration(unittest.TestCase):

    def test1(self):
        input = ["+1", "-1"]
        start_value = 0
        expected_result = 0
        actual_result = chronal_calibration_2.operate_2(input, start_value)
        self.assertEqual(expected_result, actual_result)

    def test2(self):
        input = ["+3", "+3", "+4", "-2", "-4"]
        start_value = 0
        expected_result = 10
        actual_result = chronal_calibration_2.operate_2(input, start_value)
        self.assertEqual(expected_result, actual_result)

    def test3(self):
        input = ["-6", "+3", "+8", "+5", "-6"]
        start_value = 0
        expected_result = 5
        actual_result = chronal_calibration_2.operate_2(input, start_value)
        self.assertEqual(expected_result, actual_result)

    def test4(self):
        input = ["+7", "+7", "-2", "-7", "-4"]
        start_value = 0
        expected_result = 14
        actual_result = chronal_calibration_2.operate_2(input, start_value)
        self.assertEqual(expected_result, actual_result)


if __name__ == "__main__":
    unittest.main()
