#!/usr/bin/env python

def parse_input_file(filename: str):

    with open(filename) as input_file:

        parsed_input = []
        for line in input_file.read().splitlines():
            row = []
            index = 0
            while index < len(line):
                current = line[index]
                if current in ['e', 'w']:
                    row.append(current)
                    index += 1
                else:
                    row.append(line[index:index+2])
                    index += 2
            parsed_input.append(row)
    return parsed_input


ODD_Y_MAP = {
    'w': (-1, 0),
    'e': (1, 0),
    'nw': (0, -1),
    'ne': (1, -1),
    'sw': (0, 1),
    'se': (1, 1),
}

EVEN_Y_MAP = {
    'w': (-1, 0),
    'e': (1, 0),
    'nw': (-1, -1),
    'ne': (0, -1),
    'sw': (-1, 1),
    'se': (0, 1),
}


MAP_CHOICE = {
    True: EVEN_Y_MAP,
    False: ODD_Y_MAP,
}


def is_even(y):
    return y % 2 == 0


def follow_directions(line):
    x, y = (0, 0)
    for instruction in line:
        table = MAP_CHOICE[is_even(y)]
        xmod, ymod = table[instruction]
        x += xmod
        y += ymod
    return (x, y)


def identify_black_hexes(instructions):
    destination_hexes = {}
    for instruction in instructions:
        coord = follow_directions(instruction)
        destination_hexes.setdefault(coord, 0)
        destination_hexes[coord] += 1

    black_hexes = []
    for coord, count in destination_hexes.items():
        if not is_even(count):
            black_hexes.append(coord)
    return black_hexes


def one_day_flip(tile_list):
    new_tile_list = []

    white_tile_counts = {}

    for tile in tile_list:
        x, y = tile
        table = MAP_CHOICE[is_even(y)]
        adjacent_count = 0
        for xmod, ymod in table.values():
            adjacent_coord = (x + xmod, y + ymod)
            if adjacent_coord in tile_list:
                adjacent_count += 1
            else:
                white_tile_counts.setdefault(
                    adjacent_coord, 0
                )
                white_tile_counts[adjacent_coord] += 1
        if adjacent_count in [1, 2]:
            new_tile_list.append(tile)

    for coord, count in white_tile_counts.items():
        if count == 2:
            new_tile_list.append(coord)

    return new_tile_list


def flip_for_days(tile_list, days=100):
    for x in range(0, days):
        tile_list = one_day_flip(tile_list)
    return tile_list


def main():
    parsed_input = parse_input_file("input.txt")

    part_2_input = identify_black_hexes(
        parsed_input
    )
    part_1_result = len(part_2_input)
    print(f"Part 1: {part_1_result}")

    part_2_result = len(flip_for_days(part_2_input))
    print(f"Part 2: {part_2_result}")


if __name__ == "__main__":
    main()
