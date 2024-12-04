#!/usr/bin/env python

import unittest
from . import solution


class TestSolution(unittest.TestCase):

    test_grid = [
        [3, 0, 3, 7, 3],
        [2, 5, 5, 1, 2],
        [6, 5, 3, 3, 2],
        [3, 3, 5, 4, 9],
        [3, 5, 3, 9, 0],
    ]

    def test_parse_input_file(self):
        parsed_input = solution.parse_input_file("test_input.txt")
        self.assertEqual(parsed_input, self.test_grid)

    def test_is_visible(self):
        test_cases = [
            (1, 1, True),
            (2, 1, True),
            (3, 1, False),

            (1, 2, True),
            (2, 2, False),
            (3, 2, True),

            (1, 3, False),
            (2, 3, True),
            (3, 3, False),
        ]
        for x, y, expected_result in test_cases:
            result = solution.is_visible(self.test_grid, x, y)
            self.assertEqual(result, expected_result)

    def test_count_visible(self):
        expected_result = 21
        result = solution.count_visible(self.test_grid)
        self.assertEqual(expected_result, result)

    def test_scenic_score(self):
        test_cases = [
            (2, 1, 4),
            (2, 3, 8),
        ]
        for x, y, expected_result in test_cases:
            result = solution.scenic_score(self.test_grid, x, y)
            self.assertEqual(result, expected_result)

    def test_best_scenic_score(self):
        result = solution.best_scenic_score(self.test_grid)
        expected_result = 8
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
