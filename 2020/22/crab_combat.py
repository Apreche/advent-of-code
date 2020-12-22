#!/usr/bin/env python

def parse_input_file(filename: str):

    with open(filename) as input_file:

        deck_one = []
        deck_two = []
        current_deck = deck_one
        for line in input_file.read().splitlines():
            if line == "":
                current_deck = deck_two
            elif line.isdigit():
                current_deck.append(int(line))
    return (deck_one, deck_two)


def combat_once(deck_one, deck_two):
    new_deck_one = []
    new_deck_two = []
    if deck_one[0] > deck_two[0]:
        new_deck_one = deck_one[1:] + [deck_one[0]] + [deck_two[0]]
        new_deck_two = deck_two[1:]
    elif deck_one[0] < deck_two[0]:
        new_deck_two = deck_two[1:] + [deck_two[0]] + [deck_one[0]]
        new_deck_one = deck_one[1:]
    else:
        print("WHOAH!")
    return (new_deck_one, new_deck_two)


def crab_score(deck):
    score = 0
    for index, card in enumerate(deck[::-1]):
        score += (index + 1) * card
    return score


def crab_combat(deck_one, deck_two):
    num_rounds = 0
    while (len(deck_one) > 0) and (len(deck_two) > 0):
        num_rounds += 1
        deck_one, deck_two = combat_once(
            deck_one,
            deck_two
        )
    if len(deck_one) == 0:
        return crab_score(deck_two)
    else:
        return crab_score(deck_one)


def main():
    deck_one, deck_two = parse_input_file("input.txt")

    part_1_result = crab_combat(deck_one, deck_two)
    print(f"Part 1: {part_1_result}")

    part_2_result = None
    print(f"Part 2: {part_2_result}")


if __name__ == "__main__":
    main()
