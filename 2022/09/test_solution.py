#!/usr/bin/env python

import unittest
from . import solution


class TestSolution(unittest.TestCase):

    test_instructions = [
        ("R", 4),
        ("U", 4),
        ("L", 3),
        ("D", 1),
        ("R", 4),
        ("D", 1),
        ("L", 5),
        ("R", 2),
    ]

    part_2_test_instructions = [
        ("R", 5),
        ("U", 8),
        ("L", 8),
        ("D", 3),
        ("R", 17),
        ("D", 10),
        ("L", 25),
        ("U", 20),
    ]

    def test_parse_input_file(self):
        result = solution.parse_input_file("test_input.txt")
        self.assertEqual(result, self.test_instructions)

    def test_follow(self):
        test_cases = [
            # (leader, follower, follower_new_position)
            # no movement
            (solution.Point(0, 0), solution.Point(0, 0)),
            (solution.Point(1, 0), solution.Point(0, 0)),
            (solution.Point(1, 1), solution.Point(0, 0)),
            (solution.Point(0, 1), solution.Point(0, 0)),
            (solution.Point(-1, 1), solution.Point(0, 0)),
            (solution.Point(-1, 0), solution.Point(0, 0)),
            (solution.Point(-1, -1), solution.Point(0, 0)),
            (solution.Point(0, -1), solution.Point(0, 0)),
            (solution.Point(1, -1), solution.Point(0, 0)),

            # straight movement
            (solution.Point(-2, 0), solution.Point(-1, 0)),
            (solution.Point(2, 0), solution.Point(1, 0)),
            (solution.Point(0, 2), solution.Point(0, 1)),
            (solution.Point(0, -2), solution.Point(0, -1)),

            # diagonal movement
            (solution.Point(2, 1), solution.Point(1, 1)),
            (solution.Point(2, -1), solution.Point(1, -1)),
            (solution.Point(-2, 1), solution.Point(-1, 1)),
            (solution.Point(-2, -1), solution.Point(-1, -1)),
            (solution.Point(1, 2), solution.Point(1, 1)),
            (solution.Point(1, -2), solution.Point(1, -1)),
            (solution.Point(-1, 2), solution.Point(-1, 1)),
            (solution.Point(-1, -2), solution.Point(-1, -1)),

            # big diagonal movement
            (solution.Point(2, 2), solution.Point(1, 1)),
            (solution.Point(2, -2), solution.Point(1, -1)),
            (solution.Point(-2, 2), solution.Point(-1, 1)),
            (solution.Point(-2, -2), solution.Point(-1, -1)),
        ]
        for leader, expected_result in test_cases:
            self.assertEqual(
                solution.Point(0, 0).follow(leader), expected_result
            )

    def test_part_1_answer(self):
        result = solution.process_instructions(self.test_instructions)
        expected_result = 13
        self.assertEqual(result, expected_result)

    def test_part_2_answer_a(self):
        result = solution.process_instructions(
            self.test_instructions, num_knots=10
        )
        expected_result = 1
        self.assertEqual(result, expected_result)

    def test_part_2_answer_b(self):
        result = solution.process_instructions(
            self.part_2_test_instructions, num_knots=10
        )
        expected_result = 36
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
