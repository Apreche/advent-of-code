#!/usr/bin/env python

import unittest
from . import solution


class TestSolution(unittest.TestCase):

    SMALL_INPUT = [
        "noop",
        "addx 3",
        "addx -5",
    ]

    def test_small_input(self):
        system = solution.VideoSystem(key_cycles=range(7))
        for command in self.SMALL_INPUT:
            system.process_command(command)
        expected_result = {
            1: 1,
            2: 1,
            3: 1,
            4: 4,
            5: 4,
        }
        self.assertEqual(
            system.result_cycles,
            expected_result
        )
        system.process_command("noop")
        expected_result = {
            1: 1,
            2: 1,
            3: 1,
            4: 4,
            5: 4,
            6: -1,
        }
        self.assertEqual(
            system.result_cycles,
            expected_result
        )

    def test_signal_strength(self):
        instructions = solution.parse_input_file("test_input.txt")
        key_cycles = range(20, 221, 40)
        system = solution.VideoSystem(key_cycles=key_cycles)
        for instruction in instructions:
            system.process_command(instruction)
        expected_result = 13140
        self.assertEqual(system.signal_strength, expected_result)

    def test_display(self):
        instructions = solution.parse_input_file("test_input.txt")
        system = solution.VideoSystem()
        for instruction in instructions:
            system.process_command(instruction)

        expected_result = (
            "##..##..##..##..##..##..##..##..##..##.."
            "###...###...###...###...###...###...###."
            "####....####....####....####....####...."
            "#####.....#####.....#####.....#####....."
            "######......######......######......####"
            "#######.......#######.......#######....."
        )
        result = "".join(system.display)
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
