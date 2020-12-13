#!/usr/bin/env python

def parse_input_file(filename: str):

    with open(filename) as input_file:

        parsed_input = []
        for line in input_file.read().splitlines():
            direction = line[0]
            distance = int(line[1:])
            parsed_input.append((direction, distance))
    return parsed_input


START_POSITION = (0, 0)

START_FACING = 'E'

DIRECTIONS = {
    'N': (0, 1),
    'E': (1, 0),
    'S': (0, -1),
    'W': (-1, 0),
}

ROTATIONS = {
    'L': {
        'N': {90: 'W', 180: 'S', 270: 'E'},
        'E': {90: 'N', 180: 'W', 270: 'S'},
        'S': {90: 'E', 180: 'N', 270: 'W'},
        'W': {90: 'S', 180: 'E', 270: 'N'},
    },
    'R': {
        'N': {90: 'E', 180: 'S', 270: 'W'},
        'E': {90: 'S', 180: 'W', 270: 'N'},
        'S': {90: 'W', 180: 'N', 270: 'E'},
        'W': {90: 'N', 180: 'E', 270: 'S'},
    },
}


def manhattan_distance(start, end):
    startx, starty = start
    endx, endy = end
    changex = abs(endx) - abs(startx)
    changey = abs(endy) - abs(starty)
    return changex + changey


def move(current_location, direction, distance):
    x_vec, y_vec = DIRECTIONS[direction]
    x_move = x_vec * distance
    y_move = y_vec * distance
    vector = (x_move, y_move)
    return tuple(
        map(
            sum,
            zip(current_location, vector)
        )
    )


def follow_directions(instructions):

    current_position = START_POSITION
    current_facing = START_FACING

    for instruction, distance in instructions:
        if instruction in DIRECTIONS:
            current_position = move(
                current_position,
                instruction,
                distance
            )
        elif instruction in ROTATIONS:
            current_facing = ROTATIONS[instruction][current_facing][distance]
        else:  # Must be F
            current_position = move(
                current_position,
                current_facing,
                distance
            )
    return current_position


def main():
    parsed_input = parse_input_file("input.txt")
    final_position = follow_directions(parsed_input)
    part_1_result = manhattan_distance(
        START_POSITION, final_position
    )
    print(f"Part 1: {part_1_result}")

    part_2_result = None
    print(f"Part 2: {part_2_result}")


if __name__ == "__main__":
    main()
