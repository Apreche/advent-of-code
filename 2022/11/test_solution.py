#!/usr/bin/env python

import unittest
from . import solution


class TestSolution(unittest.TestCase):

    def test_part_1(self):
        monkey_definitinos = solution.parse_input_file("test_input.txt")
        monkeys = solution.make_monkeys(monkey_definitinos)
        solution.simulate_monkeys(monkeys)
        monkey_business = solution.calculate_monkey_business(monkeys)
        expected_monkey_business = 10605
        self.assertEqual(monkey_business, expected_monkey_business)

    def test_part_2(self):
        monkey_definitions = solution.parse_input_file("test_input.txt")
        monkeys = solution.make_monkeys(
            monkey_definitions, less_worried=False
        )
        solution.simulate_monkeys(monkeys, rounds=10000)
        monkey_business = solution.calculate_monkey_business(monkeys)
        expected_monkey_business = 2713310158
        self.assertEqual(monkey_business, expected_monkey_business)


if __name__ == "__main__":
    unittest.main()
