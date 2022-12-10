#!/usr/bin/env python

import textwrap
import os


class VideoSystem():
    DISPLAY_WIDTH = 40

    def __init__(self, key_cycles=[]):
        self.cycle = 0
        self.register = 1
        self.key_cycles = key_cycles
        self.result_cycles = {}
        self.display = []

    def draw(self):
        target_position = (self.cycle) % self.DISPLAY_WIDTH
        leftmost = self.register - 1
        rightmost = self.register + 1
        if leftmost <= target_position <= rightmost:
            self.display.append("#")
        else:
            self.display.append(".")

    def print_display(self):
        text = "".join(self.display)
        wrapped_text = textwrap.wrap(text, self.DISPLAY_WIDTH)
        for row in wrapped_text:
            print(row)

    def advance_cycle(self):
        self.draw()
        self.cycle += 1
        if self.cycle in self.key_cycles:
            self.result_cycles[self.cycle] = self.register

    def noop(self, *args):
        self.advance_cycle()

    def addx(self, value):
        self.advance_cycle()
        self.advance_cycle()
        self.register += value

    def process_command(self, raw_command):
        command, *params = raw_command.split(" ")
        params = [int(n) for n in params]
        command_map = {
            "noop": self.noop,
            "addx": self.addx,
        }
        assert (command in command_map)
        command_map[command](*params)

    @property
    def signal_strength(self):
        strength = sum(
            [cycle * value for cycle, value in self.result_cycles.items()]
        )
        return strength


def parse_input_file(filename: str):
    current_dir = os.path.dirname(__file__)
    full_file_path = os.path.join(current_dir, filename)
    with open(full_file_path) as input_file:
        parsed_input = []
        for line in input_file.read().splitlines():
            parsed_input.append(line)
    return parsed_input


def main():
    instructions = parse_input_file("input.txt")

    system = VideoSystem(key_cycles=range(20, 221, 40))
    for instruction in instructions:
        system.process_command(instruction)

    part_1_result = system.signal_strength
    print(f"Part 1: {part_1_result}")

    print("Part 2:")
    system.print_display()


if __name__ == "__main__":
    main()
