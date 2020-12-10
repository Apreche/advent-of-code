#!/usr/bin/env python

def parse_input_file(filename: str):

    with open(filename) as input_file:

        parsed_input = []
        for line in input_file.read().splitlines():
            parsed_input.append(line)
    return parsed_input


def main():
    parsed_input = parse_input_file("input.txt")
    print(parsed_input)

    part_1_result = None
    print(f"Part 1: {part_1_result}")

    part_2_result = None
    print(f"Part 2: {part_2_result}")


if __name__ == "__main__":
    main()
