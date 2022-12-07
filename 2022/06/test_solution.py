#!/usr/bin/env python

import unittest
from . import solution


class TestSolution(unittest.TestCase):

    def test_find_start_packet_marker(self):
        test_cases = [
            (7, "mjqjpqmgbljsphdztnvjfqwrcgsmlb"),
            (5, "bvwbjplbgvbhsrlpgdmjqwftvncz"),
            (6, "nppdvjthqldpwncqszvftbrmjlhg"),
            (10, "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"),
            (11, "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"),
        ]
        for expected_result, input in test_cases:
            result = solution.find_start_marker(input)
            self.assertEqual(result, expected_result)

    def test_find_start_message_marker(self):
        test_cases = [
            (19, "mjqjpqmgbljsphdztnvjfqwrcgsmlb"),
            (23, "bvwbjplbgvbhsrlpgdmjqwftvncz"),
            (23, "nppdvjthqldpwncqszvftbrmjlhg"),
            (29, "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"),
            (26, "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"),
        ]
        for expected_result, input in test_cases:
            result = solution.find_start_marker(input, window=14)
            self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
