#!/usr/bin/env python

import os


class OctopusGrid:

    def __init__(self, grid):
        self.grid = grid

    def _increment_grid(self):
        for x in range(10):
            for y in range(10):
                self.grid[y][x] += 1

    def _get_adjacencies(self, coord):
        coords = []
        x, y = coord
        for xd in [-1, 0, 1]:
            for yd in [-1, 0, 1]:
                fx = x + xd
                fy = y + yd
                xgood = (fx >= 0) and (fx < 10)
                ygood = (fy >= 0) and (fy < 10)
                if xgood and ygood:
                    coords.append((x + xd, y + yd))
        coords.remove((x, y))
        return coords

    def _process_flashes(self):
        flash_count = 0

        flashed_coords = []
        for x in range(10):
            for y in range(10):
                if self.grid[y][x] > 9:
                    flashed_coords.append((x, y))
                    self.grid[y][x] = 0
        if len(flashed_coords) == 0:
            return flash_count

        for coord in flashed_coords:
            for adjcoord in self._get_adjacencies(coord):
                x, y = adjcoord
                if self.grid[y][x] != 0:
                    self.grid[y][x] += 1
        flash_count = len(flashed_coords)
        flash_count += self._process_flashes()
        return flash_count

    def step(self):
        self._increment_grid()
        return self._process_flashes()

    def display_grid(self):
        for row in self.grid:
            print("".join([str(x) for x in row]))

    def steps(self, num_steps):
        count = 0
        for _ in range(num_steps):
            count += self.step()
        return count


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
    octopus_grid = OctopusGrid(parsed_input)

    part_1_result = octopus_grid.steps(100)
    print(f"Part 1: {part_1_result}")

    part_2_result = None
    print(f"Part 2: {part_2_result}")


if __name__ == "__main__":
    main()
