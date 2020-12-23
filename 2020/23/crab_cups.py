#!/usr/bin/env python

TEST_INPUT = [3, 8, 9, 1, 2, 5, 4, 6, 7]
TEST_ANSWER_ONE = 67384529
TEST_ANSWER_TWO = 149245887792
INPUT = [8, 7, 2, 4, 9, 5, 1, 3, 6]


def crab_moves(cups=[], num_moves=100):
    current_move = 0
    current_cup = cups[0]
    size = len(cups)

    while current_move < num_moves:
        # next move
        current_move += 1

        # find current cup
        current_cup_index = cups.index(current_cup)

        # pickup next 3 clockwise cups
        if size - current_cup_index >= 4:
            pickups = cups[current_cup_index + 1:current_cup_index + 4]
        elif size - current_cup_index == 3:
            pickups = cups[current_cup_index + 1:] + cups[0:1]
        elif size - current_cup_index == 2:
            pickups = cups[current_cup_index + 1:] + cups[0:2]
        elif size - current_cup_index == 1:
            pickups = cups[current_cup_index + 1:] + cups[0:3]

        for pick in pickups:
            cups.remove(pick)

        # identify destination cup
        destination_cup = None
        seeking_cup = current_cup - 1
        while destination_cup is None and seeking_cup > 0:
            if seeking_cup not in pickups:
                destination_cup = seeking_cup
            else:
                seeking_cup -= 1

        if destination_cup is None:
            destination_cup = max(cups)

        # reinsert removed cups
        destination_index = cups.index(destination_cup) + 1
        pickups.reverse()
        for pick in pickups:
            cups.insert(destination_index, pick)

        # identify new current_cup
        new_current_index = cups.index(current_cup) + 1
        if new_current_index == size:
            current_cup = cups[0]
        else:
            current_cup = cups[new_current_index]

    return cups


def get_part_one_answer(cups):
    index = cups.index(1)
    after_one = cups[index + 1:] + cups[:index]
    after_one = [str(x) for x in after_one]
    return int(''.join(after_one))


def get_part_two_answer(cups):
    num_cups = len(cups)
    index = cups.index(1)
    if num_cups - 1 == index:
        return cups[0] * cups[1]
    elif num_cups - 2 == index:
        return cups[-1] * cups[0]
    return cups[index+1] * cups[index+2]


def main():
    test_one_cups = crab_moves(TEST_INPUT, num_moves=100)
    test_one_result = get_part_one_answer(test_one_cups)
    assert(test_one_result == TEST_ANSWER_ONE)

    part_1_cups = crab_moves(INPUT)
    part_1_result = get_part_one_answer(part_1_cups)
    print(f"Part 1: {part_1_result}")

    ONE_MILLION = 1000000
    TEN_MILLION = ONE_MILLION * 10

    test_two_input = TEST_INPUT + list(
        range(max(TEST_INPUT) + 1, ONE_MILLION + 1)
    )
    assert(len(test_two_input) == ONE_MILLION)
    test_two_cups = crab_moves(
        test_two_input, TEN_MILLION
    )
    test_two_result = get_part_two_answer(test_two_cups)
    assert(test_two_result == TEST_ANSWER_TWO)

    part_2_input = INPUT + list(
        range(max(INPUT) + 1,  + 1)
    )
    part_2_cups = crab_moves(
        part_2_input, TEN_MILLION
    )
    part_2_result = get_part_two_answer(part_2_cups)
    print(f"Part 2: {part_2_result}")


if __name__ == "__main__":
    main()
