#!/usr/bin/env python

INSTRUCTIONS = {
    'R': (1, 0),
    'U': (0, 1),
    'L': (-1, 0),
    'D': (0, -1),
}

def cartesian_add(c1, c2):
    x1, y1 = c1
    x2, y2 = c2
    return (x1 + x2, y1 + y2)

def manhattan_distance(coordinate):
    x, y = coordinate
    return abs(x) + abs(y)

def make_wire(instructions):
    current_location = (0,0)
    locations = []
    for instruction in instructions:
        direction = instruction[0]
        count = int(instruction[1:])
        for index in range(count):
            new_location = cartesian_add(
                current_location,
                INSTRUCTIONS[direction]
            )
            locations.append(new_location)
            current_location = new_location
    return locations

if __name__ == "__main__":
    with open('input.txt', 'r') as input_file:
        wire_instructions = input_file.read().splitlines()

    wire_a = make_wire(wire_instructions[0].split(','))
    wire_b = make_wire(wire_instructions[1].split(','))
    intersections = set(wire_a).intersection(wire_b)

    distances = []
    for intersection in intersections:
        distances.append(manhattan_distance(intersection))
    shortest = sorted(distances)[0]
    print(f"Distance to closest intersection: {shortest}")

    distances = []
    for intersection in intersections:
        a_steps = wire_a.index(intersection) + 1
        b_steps = wire_b.index(intersection) + 1
        distances.append(a_steps + b_steps)
    shortest = sorted(distances)[0]
    print(f"Combined steps to intersection: {shortest}")
