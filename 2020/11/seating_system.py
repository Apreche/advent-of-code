#!/usr/bin/env python

# (is_seat, is_occupied)

def parse_input_file(filename: str):

    with open(filename) as input_file:
        parsed_input = []
        for line in input_file.read().splitlines():
            row = []
            for char in line:
                if char == 'L':
                    row.append((True, False))
                else:
                    row.append((False, False))
            parsed_input.append(row)
    return parsed_input


def adjacency_count(seating_area, row, col):

    min_row = 0
    min_col = 0
    max_row = len(seating_area) - 1
    max_col = len(seating_area[0]) - 1

    check_locations = [
        (row+1, col),
        (row-1, col),
        (row, col+1),
        (row, col-1),
        (row+1, col+1),
        (row-1, col-1),
        (row-1, col+1),
        (row+1, col-1)
    ]

    adjacencies = 0
    for x, y in check_locations:
        x_oob = (x < min_row) or (x > max_row)
        y_oob = (y < min_col) or (y > max_col)
        if x_oob or y_oob:
            continue
        if seating_area[x][y][1]:
            adjacencies += 1
    return adjacencies


def process_rules(seating_area):
    num_changes = 0
    new_seating_area = []
    for row_num, row in enumerate(seating_area):
        new_row = []
        for col_num, spot in enumerate(row):
            is_seat, is_occupied = spot
            if not is_seat:
                new_row.append(spot)
                continue
            num_adjacencies = adjacency_count(
                seating_area, row_num, col_num
            )
            if (not is_occupied) and (num_adjacencies == 0):
                new_row.append((True, True))
                num_changes += 1
            elif is_occupied and (num_adjacencies >= 4):
                new_row.append((True, False))
                num_changes += 1
            else:
                new_row.append(spot)
        new_seating_area.append(new_row)
    return (num_changes, new_seating_area)


def count_occupied_seats(seating_area):
    occupied = 0
    for row in seating_area:
        for seat in row:
            if seat[1]:
                occupied += 1
    return occupied


def part_1_process(seating_area):
    num_changes = None
    while num_changes != 0:
        num_changes, new_seating_area = process_rules(
            seating_area
        )
        seating_area = new_seating_area
    return count_occupied_seats(seating_area)


def print_seating_area(seating_area):
    display_area = []
    for row in seating_area:
        display_row = []
        for is_seat, is_occupied in row:
            if not is_seat:
                display_row.append('.')
            elif is_occupied:
                display_row.append('#')
            else:
                display_row.append('L')
        display_area.append("".join(display_row))
    print("\n".join(display_area))


def main():
    original_seating_area = parse_input_file("input.txt")

    part_1_result = part_1_process(original_seating_area)
    print(f"Part 1: {part_1_result}")

    part_2_result = None
    print(f"Part 2: {part_2_result}")


if __name__ == "__main__":
    main()
