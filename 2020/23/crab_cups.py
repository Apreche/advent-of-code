#!/usr/bin/env python

TEST_INPUT = [3, 8, 9, 1, 2, 5, 4, 6, 7]
TEST_ANSWER = "67384529"
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
        destination_cup = max(cups)
        lesser_cups = [lc for lc in cups if lc < current_cup]
        if lesser_cups:
            destination_cup = max(lesser_cups)

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


def get_answer(cups):
    index = cups.index(1)
    after_one = cups[index + 1:] + cups[:index]
    after_one = [str(x) for x in after_one]
    return ''.join(after_one)


def main():
    test_cups = crab_moves(TEST_INPUT, num_moves=100)
    test_result = get_answer(test_cups)
    assert(test_result == TEST_ANSWER)

    part_1_cups = crab_moves(INPUT)
    part_1_result = get_answer(part_1_cups)
    print(f"Part 1: {part_1_result}")

    part_2_result = None
    print(f"Part 2: {part_2_result}")


if __name__ == "__main__":
    main()
