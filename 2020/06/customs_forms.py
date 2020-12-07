#!/usr/bin/env python


def parse_input_file(filename: str):
    groups = []
    with open(filename) as input_file:
        current_group = ''
        group_size = 0
        for line in input_file.read().splitlines():
            if len(line) > 0:
                current_group += line
                group_size += 1
            else:
                groups.append(
                    (current_group, group_size)
                )
                current_group = ''
                group_size = 0
        groups.append(
            (current_group, group_size)
        )

    return groups


def count_group(group):
    return len(set(group))


def count_all_groups(groups):
    return sum([count_group(group) for group in groups])


def count_group_2(group):
    group_string, group_count = group
    total_count = 0
    for char in set(group_string):
        if(group_string.count(char) == group_count):
            total_count += 1
    return total_count


def count_all_groups_2(groups):
    return sum([count_group_2(group) for group in groups])


def main():
    part_2_data = parse_input_file('input.txt')
    part_1_data = [data[0] for data in part_2_data]
    result_1 = count_all_groups(part_1_data)
    print(f"Part 1: {result_1}")
    result_2 = count_all_groups_2(part_2_data)
    print(f"Part 2: {result_2}")


if __name__ == "__main__":
    main()
