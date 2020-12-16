#!/usr/bin/env python

PART_1_TESTS = {
    (1, 3, 2): 1,
    (2, 1, 3): 10,
    (1, 2, 3): 27,
    (2, 3, 1): 78,
    (3, 2, 1): 438,
    (3, 1, 2): 1836,
}

PART_2_TESTS = {
    (0, 3, 6): 175594,
    (1, 3, 2): 2578,
    (2, 1, 3): 3544142,
    (1, 2, 3): 261214,
    (2, 3, 1): 6895259,
    (3, 2, 1): 18,
    (3, 1, 2): 362,
}


INPUT = [1, 0, 15, 2, 10, 13]


def get_xth_spoken(starting_numbers, iterations=2020):
    starting_numbers = list(starting_numbers)
    last_appearance_lookup = {}
    for number in starting_numbers[:-1]:
        last_appearance = len(starting_numbers) - starting_numbers[::-1].index(number)
        last_appearance_lookup[number] = last_appearance

    game = starting_numbers
    while len(game) < iterations:
        newest = game[-1]
        if newest not in last_appearance_lookup:
            val = 0
        else:

            latest_appearance = last_appearance_lookup[newest]
            val = len(game) - latest_appearance
        last_appearance_lookup[newest] = len(game)
        game.append(val)

    return game[-1]


def main():
    # Part 1 Test Framework
    for test_tuple, answer in PART_1_TESTS.items():
        test_data = list(test_tuple)
        test_result = get_xth_spoken(test_data)
        assert(test_result == answer)

    part_1_result = get_xth_spoken(INPUT)
    print(f"Part 1: {part_1_result}")

    # Part 2 Test Framework
    for test_data, answer in PART_2_TESTS.items():
        test_result = get_xth_spoken(
            test_data, iterations=30000000
        )
        assert(test_result == answer)

    part_2_result = get_xth_spoken(
        INPUT, iterations=30000000
    )
    print(f"Part 2: {part_2_result}")


if __name__ == "__main__":
    main()
