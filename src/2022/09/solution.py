#!/usr/bin/env python
from __future__ import annotations

import dataclasses
import os
import typing


def sign(number):
    if number == 0:
        return 0
    elif number > 0:
        return 1
    else:
        return -1


@dataclasses.dataclass
class Point:
    x: int
    y: int

    DIRECTIONS: typing.ClassVar[dict] = {
        "R": (1, 0),
        "L": (-1, 0),
        "U": (0, 1),
        "D": (0, -1),
    }

    def __iter__(self):
        for i in (self.x, self.y):
            yield i

    def is_far_from(self, point: Point) -> int:
        x_far = abs(self.x - point.x) > 1
        y_far = abs(self.y - point.y) > 1
        return x_far or y_far

    def move(self, instruction) -> None:
        dx, dy = self.DIRECTIONS[instruction]
        self.x += dx
        self.y += dy

    def follow(self, point) -> Point:
        dx = point.x - self.x
        dy = point.y - self.y
        abxy = [abs(dx), abs(dy)]
        assert (not any([t for t in abxy if t > 2]))

        if 2 not in abxy:
            return self

        self.y += sign(dy)
        self.x += sign(dx)
        return self


def parse_input_file(filename: str):
    current_dir = os.path.dirname(__file__)
    full_file_path = os.path.join(current_dir, filename)
    with open(full_file_path) as input_file:
        parsed_input = []
        for line in input_file.read().splitlines():
            direction, distance = line.split(" ")
            parsed_input.append(
                (direction, int(distance))
            )
    return parsed_input


def print_rope(points=[]) -> None:
    all_x = [p.x for p in points]
    min_x = min(all_x)
    max_x = max(all_x)
    all_y = [p.y for p in points]
    min_y = min(all_y)
    max_y = max(all_y)
    for y in range(max_y+1, min_y-2, -1):
        row = []
        for x in range(min_x-1, max_x+2):
            point = Point(x, y)
            if point in points:
                row.append(str(points.index(point)))
            else:
                row.append(".")
        print("".join(row))
    print("***")


def check_rope(rope) -> bool:
    "verify the rope isn't broken"
    for i in range(len(rope) - 1):
        if rope[i].is_far_from(rope[i+1]):
            return False
    return True


def process_instructions(instructions, num_knots=2) -> int:
    rope = [Point(0, 0) for _ in range(num_knots)]

    tail_positions = [(rope[-1].x, rope[-1].y)]

    count = 0
    for direction, distance in instructions:
        count += 1
        for _ in range(distance):
            rope[0].move(direction)
            for i in range(num_knots-1):
                rope[i+1].follow(rope[i])
            tail_positions.append(
                (rope[-1].x, rope[-1].y)
            )
            assert (check_rope(rope))
    return len(set(tail_positions))


def main() -> None:
    instructions = parse_input_file("input.txt")

    part_1_result = process_instructions(instructions)
    print(f"Part 1: {part_1_result}")

    part_2_result = process_instructions(
        instructions, num_knots=10
    )
    print(f"Part 2: {part_2_result}")


if __name__ == "__main__":
    main()
