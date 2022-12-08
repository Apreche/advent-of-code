#!/usr/bin/env python

import unittest
from . import solution


class TestSolution(unittest.TestCase):

    def test_dirsize(self):
        parsed_input = solution.parse_input_file("test_input.txt")
        filesystem = solution.create_filesystem(parsed_input)
        self.assertEqual(
            filesystem.dirsize,
            48381165
        )
        filesystem.cd("d")
        self.assertEqual(
            filesystem.dirsize,
            24933642
        )
        filesystem.cd("..")
        filesystem.cd("a")
        self.assertEqual(
            filesystem.dirsize,
            94853
        )
        filesystem.cd("e")
        self.assertEqual(
            filesystem.dirsize,
            584
        )

    def test_sum_limited_dir_sizes(self):
        parsed_input = solution.parse_input_file("test_input.txt")
        filesystem = solution.create_filesystem(parsed_input)
        filesystem.cd("/")
        total_size, limited_sizes = filesystem.sum_limited_dir_sizes(
            max_limit=100000
        )
        self.assertEqual(
            total_size,
            48381165
        )
        self.assertEqual(
            sum(limited_sizes),
            95437
        )

    def test_fine_deletable_directory(self):
        parsed_input = solution.parse_input_file("test_input.txt")
        filesystem = solution.create_filesystem(parsed_input)
        filesystem.cd("/")
        result = solution.find_deletable_directory(filesystem)
        self.assertEqual(result, 24933642)


if __name__ == "__main__":
    unittest.main()
