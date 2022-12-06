#!/usr/bin/env python

import unittest
from . import solution


class TestSolution(unittest.TestCase):

    expected_raw_stacks = [
        "    [D]",
        "[N] [C]",
        "[Z] [M] [P]",
        " 1   2   3",
    ]

    expected_raw_instructions = [
        "move 1 from 2 to 1",
        "move 3 from 1 to 3",
        "move 2 from 2 to 1",
        "move 1 from 1 to 2",
    ]

    expected_parsed_stacks = [
        ["Z", "N"],
        ["M", "C", "D"],
        ["P"],
    ]

    expected_parsed_instructions = [
        (1, 2, 1),
        (3, 1, 3),
        (2, 2, 1),
        (1, 1, 2),
    ]

    expected_modified_stacks_9000 = [
        ["C"],
        ["M"],
        ["P", "D", "N", "Z"],
    ]

    expected_modified_stacks_9001 = [
        ["M"],
        ["C"],
        ["P", "Z", "N", "D"],
    ]

    def test_parse_input_file(self):
        raw_stacks, raw_instructions = solution.parse_input_file(
            "test_input.txt")
        self.assertEqual(raw_stacks, self.expected_raw_stacks)
        self.assertEqual(raw_instructions, self.expected_raw_instructions)

    def test_parse_starting_stacks(self):
        parsed_stacks = solution.parse_stacks(
            self.expected_raw_stacks
        )
        self.assertEqual(parsed_stacks, self.expected_parsed_stacks)

    def test_parse_instructions(self):
        parsed_instructions = solution.parse_instructions(
            self.expected_raw_instructions
        )
        self.assertEqual(
            parsed_instructions,
            self.expected_parsed_instructions
        )

    def test_execute_instructions_9000(self):
        modified_stacks = solution.execute_instructions_9000(
            self.expected_parsed_stacks,
            self.expected_parsed_instructions,
        )
        self.assertEqual(modified_stacks, self.expected_modified_stacks_9000)

    def test_execute_instructions_9001(self):
        modified_stacks = solution.execute_instructions_9001(
            self.expected_parsed_stacks,
            self.expected_parsed_instructions,
        )
        self.assertEqual(modified_stacks, self.expected_modified_stacks_9001)

    def test_read_top_crates(self):
        top_crates = solution.read_top_crates(
            self.expected_modified_stacks_9000
        )
        self.assertEqual(
            top_crates,
            ["C", "M", "Z"]
        )


if __name__ == "__main__":
    unittest.main()
