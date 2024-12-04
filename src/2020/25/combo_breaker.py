#!/usr/bin/env python

TEST_PUBLIC_KEY = 5764801
CARD_PUBLIC_KEY = 18499292
DOOR_PUBLIC_KEY = 8790390


def find_loop_size(
    target_key,
    subject=7,
    starting_value=1,
):
    value = starting_value
    loop_size = 0
    while value != target_key:
        value = value * subject
        value = value % 20201227
        loop_size += 1
    return loop_size


def find_encryption_key(
    public_key,
    loop_size,
    starting_value=1,
):
    value = starting_value
    loop_count = 0
    while loop_count < loop_size:
        value = value * public_key
        value = value % 20201227
        loop_count += 1
    return value


def main():

    test_loop_size = find_loop_size(TEST_PUBLIC_KEY)
    assert(test_loop_size == 8)

    card_loop_size = find_loop_size(CARD_PUBLIC_KEY)
    door_loop_size = find_loop_size(DOOR_PUBLIC_KEY)

    card_encryption_key = find_encryption_key(
        DOOR_PUBLIC_KEY, card_loop_size
    )
    door_encryption_key = find_encryption_key(
        CARD_PUBLIC_KEY, door_loop_size
    )
    assert(card_encryption_key == door_encryption_key)
    part_1_result = card_encryption_key
    print(f"Part 1: {part_1_result}")

    # part_2_result = None
    # print(f"Part 2: {part_2_result}")


if __name__ == "__main__":
    main()
