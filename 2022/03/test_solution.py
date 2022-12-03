#!/usr/bin/env python

import unittest
from . import solution


class TestSolution(unittest.TestCase):

    original_test_input = [
        "vJrwpWtwJgWrhcsFMMfFFhFp",
        "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
        "PmmdzqPrVvPwwTWBwg",
        "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
        "ttgJtRGJQctTZtZT",
        "CrZsJsPPZsGzwwsLwLmpwMDw",
    ]

    def test_part_1(self):
        expected_result = 157
        result = solution.calculate_part_1(self.original_test_input)
        self.assertEqual(result, expected_result)

    def test_part_2(self):
        expected_result = 70
        result = solution.calculate_part_2(self.original_test_input)
        self.assertEqual(result, expected_result)

    def test_get_priority(self):
        priority_test_data = [
            ("p", 16),
            ("L", 38),
            ("P", 42),
            ("v", 22),
            ("t", 20),
            ("s", 19),
        ]
        for letter, expected_priority in priority_test_data:
            priority = solution.get_priority(letter)
            self.assertEqual(priority, expected_priority)

    def test_find_common_item(self):
        common_item_test_data = [
            (("vJrwpWtwJgWr", "hcsFMMfFFhFp",), "p",),
            (("jqHRNqRjqzjGDLGL", "rsFMfFZSrLrFZsSL",), "L",),
            (("PmmdzqPrV", "vPwwTWBwg",), "P",),
            (("wMqvLMZHhHMvwLH", "jbvcjnnSBnvTQFn",), "v",),
            (("ttgJtRGJ", "QctTZtZT",), "t",),
            (("CrZsJsPPZsGz", "wwsLwLmpwMDw",), "s",),
        ]
        for compartments, expected_item in common_item_test_data:
            common_item = solution.find_common_item(compartments)
            self.assertEqual(common_item, expected_item)

    def test_halve_sacks(self):
        expected_result = [
            ("vJrwpWtwJgWr", "hcsFMMfFFhFp",),
            ("jqHRNqRjqzjGDLGL", "rsFMfFZSrLrFZsSL",),
            ("PmmdzqPrV", "vPwwTWBwg",),
            ("wMqvLMZHhHMvwLH", "jbvcjnnSBnvTQFn",),
            ("ttgJtRGJ", "QctTZtZT",),
            ("CrZsJsPPZsGz", "wwsLwLmpwMDw",),
        ]
        result = solution.halve_sacks(self.original_test_input)
        self.assertEqual(result, expected_result)

    def test_group_sacks_by_n(self):
        expected_result = [
            [
                "vJrwpWtwJgWrhcsFMMfFFhFp",
                "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
                "PmmdzqPrVvPwwTWBwg",
            ],
            [
                "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
                "ttgJtRGJQctTZtZT",
                "CrZsJsPPZsGzwwsLwLmpwMDw",
            ]
        ]
        result = solution.group_sacks_by_n(
            self.original_test_input, 3
        )
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
