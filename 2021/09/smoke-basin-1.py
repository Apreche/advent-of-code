#!/usr/bin/env python

import os


class Basin:
    def __init__(self, grid):
        self.grid = grid
        self.height = len(grid)
        self.width = len(grid[0])

    def get_low_points(self):
        low_points = {}
        for y in range(0, self.height):
            for x in range(0, self.width):
                local_value = self.grid[y][x]
                adjacent_values = []
                if y > 0:
                    adjacent_values.append(
                        self.grid[y-1][x]
                    )
                if y < self.height - 1:
                    adjacent_values.append(
                        self.grid[y+1][x]
                    )
                if x > 0:
                    adjacent_values.append(
                        self.grid[y][x-1]
                    )
                if x < self.width - 1:
                    adjacent_values.append(
                        self.grid[y][x+1]
                    )
                if min(adjacent_values) > local_value:
                    low_points[(x, y)] = local_value
        return low_points


def parse_input_file(filename: str):
    current_dir = os.path.dirname(__file__)
    full_file_path = os.path.join(current_dir, filename)
    with open(full_file_path) as input_file:
        parsed_input = []
        for line in input_file.read().splitlines():
            parsed_input.append([int(x) for x in line])
    return parsed_input


def main():
    parsed_input = parse_input_file("input.txt")
    basin = Basin(parsed_input)
    low_points = basin.get_low_points()

    part_1_result = sum(low_points.values()) + len(low_points)
    print(f"Part 1: {part_1_result}")

    part_2_result = None
    print(f"Part 2: {part_2_result}")


if __name__ == "__main__":
    main()
