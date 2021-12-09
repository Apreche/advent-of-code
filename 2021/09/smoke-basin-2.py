#!/usr/bin/env python

import math
import os


class Basins:
    def __init__(self, grid):
        self.grid = grid
        self.height = len(grid)
        self.width = len(grid[0])
        self.low_points = None
        self.basins = []

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
                if y < (self.height - 1):
                    adjacent_values.append(
                        self.grid[y+1][x]
                    )
                if x > 0:
                    adjacent_values.append(
                        self.grid[y][x-1]
                    )
                if x < (self.width - 1):
                    adjacent_values.append(
                        self.grid[y][x+1]
                    )
                if min(adjacent_values) > local_value:
                    low_points[(x, y)] = local_value
        self.low_points = low_points
        return low_points

    def _fill_basin(self, basin, node):
        # https://en.wikipedia.org/wiki/Flood_fill
        x, y = node
        if x < 0:
            return set()
        if x > (self.width - 1):
            return set()
        if y < 0:
            return set()
        if y > (self.height - 1):
            return set()
        if node in basin:
            return set()
        if self.grid[y][x] == 9:
            return set()
        basin.add((x, y))
        for point in self._fill_basin(basin, (x+1, y)):
            basin.add(point)
        for point in self._fill_basin(basin, (x-1, y)):
            basin.add(point)
        for point in self._fill_basin(basin, (x, y-1)):
            basin.add(point)
        for point in self._fill_basin(basin, (x, y+1)):
            basin.add(point)
        return basin

    def get_basins(self):
        low_points = self.low_points or self.get_low_points()
        basins = []
        for low_point in low_points.keys():
            basin = set()
            self._fill_basin(basin, low_point)
            basins.append(basin)
        self.basins = basins
        return basins


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
    basins = Basins(parsed_input)
    low_points = basins.get_low_points()

    part_1_result = sum(low_points.values()) + len(low_points)
    print(f"Part 1: {part_1_result}")

    basins = basins.get_basins()
    basin_sizes = [len(basin) for basin in basins]
    basin_sizes.sort()
    part_2_result = math.prod(basin_sizes[-3:])
    print(f"Part 2: {part_2_result}")


if __name__ == "__main__":
    main()
