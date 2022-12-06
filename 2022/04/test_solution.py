#!/usr/bin/env python

import unittest
from . import solution


class TestSolution(unittest.TestCase):

    expected_parsed_test_input = [
        ((2, 4), (6, 8)),
        ((2, 3), (4, 5)),
        ((5, 7), (7, 9)),
        ((2, 8), (3, 7)),
        ((6, 6), (4, 6)),
        ((2, 6), (4, 8)),
    ]

    def test_parse_input(self):
        parsed_test_input = solution.parse_input_file("test_input.txt")
        self.assertEqual(
            parsed_test_input,
            self.expected_parsed_test_input
        )

    def test_is_pair_fully_contained(self):
        expected_results = [
            False,
            False,
            False,
            True,
            True,
            False,
        ]

        for index, pair in enumerate(self.expected_parsed_test_input):
            self.assertEqual(
                solution.is_pair_fully_contained(pair),
                expected_results[index]
            )

    def test_is_pair_overlapping(self):
        expected_results = [
            False,
            False,
            True,
            True,
            True,
            True,
        ]

        for index, pair in enumerate(self.expected_parsed_test_input):
            self.assertEqual(
                solution.is_pair_overlapping(pair),
                expected_results[index]
            )

    def test_count_fully_contains(self):
        expected_result = 2
        result = solution.count_fully_contains(
            self.expected_parsed_test_input
        )
        self.assertEqual(
            result, expected_result
        )

    def test_count_overlapping(self):
        expected_result = 4
        result = solution.count_overlapping(
            self.expected_parsed_test_input
        )
        self.assertEqual(
            result, expected_result
        )


if __name__ == "__main__":
    unittest.main()
