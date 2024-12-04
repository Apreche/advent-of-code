#!/usr/bin/env python

import unittest
from . import solution


class TestSolution(unittest.TestCase):
    correct_left_list = [3, 4, 2, 1, 3, 3]
    correct_right_list = [4, 3, 5, 3, 9, 3]
    correct_tuple_list = [
        (1, 3),
        (2, 3),
        (3, 3),
        (3, 4),
        (3, 5),
        (4, 9),
    ]
    correct_distance_list = [2, 1, 0, 1, 2, 5]

    def test_input_to_lists(self):
        id_lists = solution.parse_input_file("test_input.txt")
        left_list, right_list = solution.input_to_lists(id_lists)
        self.assertEqual(left_list, self.correct_left_list)
        self.assertEqual(right_list, self.correct_right_list)

    def test_lists_to_sorted_tuples(self):
        result = solution.lists_to_sorted_tuples(
            self.correct_left_list, self.correct_right_list
        )
        self.assertEqual(result, self.correct_tuple_list)

    def test_distance(self):
        tests = {
            (0, 5): 5,
            (-5, 3): 8,
            (1, 7): 6,
        }
        for params, answer in tests.items():
            result = solution.distance(*params)
            self.assertEqual(result, answer)

    def test_distance_list(self):
        result = solution.distance_list(self.correct_tuple_list)
        self.assertEqual(result, self.correct_distance_list)

    def test_total_list_distance(self):
        result = solution.total_list_distance(
            self.correct_left_list, self.correct_right_list
        )
        self.assertEqual(result, 11)

    def test_similarity_score(self):
        score = solution.similarity_score(
            self.correct_left_list, self.correct_right_list
        )
        self.assertEqual(score, 31)


if __name__ == "__main__":
    unittest.main()
