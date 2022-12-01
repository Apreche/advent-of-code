#!/usr/bin/env python

import unittest
from . import solution


class TestSolution(unittest.TestCase):

    inventory_list = [
        "1000",
        "2000",
        "3000",
        "",
        "4000",
        "",
        "5000",
        "6000",
        "",
        "7000",
        "8000",
        "9000",
        "",
        "10000",
    ]

    def test_part_1(self):
        result = solution.elf_with_most(self.inventory_list)
        self.assertEqual(result, 24000)

    def test_part_2(self):
        result = solution.top_three_total(self.inventory_list)
        self.assertEqual(result, 45000)


if __name__ == "__main__":
    unittest.main()
