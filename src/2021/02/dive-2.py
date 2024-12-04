#!/usr/bin/env python

import os


def parse_input_file(filename: str):
    current_dir = os.path.dirname(__file__)
    full_file_path = os.path.join(current_dir, filename)
    with open(full_file_path) as input_file:
        parsed_input = []
        for line in input_file.read().splitlines():
            direction, value = line.split(' ')
            value = int(value)
            parsed_input.append((direction, value))
    return parsed_input


class Submarine:
    def __init__(self):
        self.position = 0
        self.depth = 0

    def forward(self, x):
        self.position += x

    def up(self, x):
        self.depth = max(0, self.depth - x)

    def down(self, x):
        self.depth += x

    def pilot_submarine(self, directions):
        instructions = {
            'forward': self.forward,
            'up': self.up,
            'down': self.down,
        }

        for command, value in directions:
            instructions[command](value)


class BetterSubmarine(Submarine):
    def __init__(self):
        super().__init__()
        self.aim = 0

    def forward(self, x):
        self.position += x
        self.depth += self.aim * x

    def up(self, x):
        self.aim -= x

    def down(self, x):
        self.aim += x


def main():
    parsed_input = parse_input_file("input.txt")
    part1_submarine = Submarine()
    part1_submarine.pilot_submarine(parsed_input)
    part_1_result = part1_submarine.position * part1_submarine.depth
    print(f"Part 1: {part_1_result}")

    part2_submarine = BetterSubmarine()
    part2_submarine.pilot_submarine(parsed_input)
    part_2_result = part2_submarine.position * part2_submarine.depth
    print(f"Part 2: {part_2_result}")


if __name__ == "__main__":
    main()
