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


def crab_score(deck):
    score = 0
    for index, card in enumerate(deck[::-1]):
        score += (index + 1) * card
    return score


def combat_once(deck_one, deck_two):
    new_deck_one = []
    new_deck_two = []
    if deck_one[0] > deck_two[0]:
        new_deck_one = deck_one[1:] + [deck_one[0]] + [deck_two[0]]
        new_deck_two = deck_two[1:]
    elif deck_one[0] < deck_two[0]:
        new_deck_two = deck_two[1:] + [deck_two[0]] + [deck_one[0]]
        new_deck_one = deck_one[1:]
    return (new_deck_one, new_deck_two)


def crab_combat(deck_one, deck_two):
    num_rounds = 0
    while (len(deck_one) > 0) and (len(deck_two) > 0):
        num_rounds += 1
        deck_one, deck_two = combat_once(
            deck_one,
            deck_two
        )
    if len(deck_one) == 0:
        return 2, deck_two
    else:
        return 1, deck_one


def recursive_crab_combat(deck_one, deck_two):
    seen_decks = []
    special_end = False
    while (len(deck_one) > 0) and (len(deck_two) > 0):
        # special end checker
        if((deck_one, deck_two) in seen_decks):
            special_end = True
            break

        # play round normally
        seen_decks.append((deck_one, deck_two))
        new_deck_one = []
        new_deck_two = []
        round_winner = 1
        if (
                (deck_one[0] < len(deck_one)) and
                (deck_two[0] < len(deck_two))
        ):
            sub_game_winner, winning_deck = recursive_crab_combat(
                deck_one[1:1 + deck_one[0]],
                deck_two[1:1 + deck_two[0]],
            )
            round_winner = sub_game_winner
        elif deck_one[0] > deck_two[0]:
            round_winner = 1
        elif deck_one[0] < deck_two[0]:
            round_winner = 2

        if round_winner == 1:
            new_deck_one = deck_one[1:] + [deck_one[0]] + [deck_two[0]]
            new_deck_two = deck_two[1:]
        elif round_winner == 2:
            new_deck_two = deck_two[1:] + [deck_two[0]] + [deck_one[0]]
            new_deck_one = deck_one[1:]
        deck_one, deck_two = new_deck_one, new_deck_two

    if special_end or len(deck_two) == 0:
        return 1, deck_one
    else:
        return 2, deck_two


def main():
    deck_one, deck_two = parse_input_file("input.txt")
    part_1_winner, part_1_deck = crab_combat(
        deck_one, deck_two
    )
    part_1_result = crab_score(part_1_deck)
    print(f"Part 1: {part_1_result}")

    part_2_winner, part_2_deck = recursive_crab_combat(
        deck_one, deck_two
    )

    part_2_result = crab_score(part_2_deck)
    print(f"Part 2: {part_2_result}")


if __name__ == "__main__":
    main()
