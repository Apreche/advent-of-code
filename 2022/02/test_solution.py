#!/usr/bin/env python

import unittest
from . import solution


class TestSolution(unittest.TestCase):

    test_input = [
        ("A", "Y"),
        ("B", "X"),
        ("C", "Z"),
    ]

    def test_tournament(self):
        result = solution.rps_tournament(self.test_input)
        self.assertEqual(result, 15)

    def test_input_translator(self):
        translated_data = solution.part_2_input_translator(self.test_input)
        expected_data = [
            ("A", "X"),
            ("B", "X"),
            ("C", "X"),
        ]
        self.assertEqual(
            translated_data,
            expected_data,
        )

    def test_translated_tournament(self):
        translated_data = solution.part_2_input_translator(self.test_input)
        result = solution.rps_tournament(translated_data)
        self.assertEqual(result, 12)


if __name__ == "__main__":
    unittest.main()
