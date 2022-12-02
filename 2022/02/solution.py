#!/usr/bin/env python

import os
import typing

from dataclasses import dataclass


@dataclass
class RPSGame:
    ROCK: typing.ClassVar[str] = "Rock"
    PAPER: typing.ClassVar[str] = "Paper"
    SCISSORS: typing.ClassVar[str] = "Scissors"
    WIN: typing.ClassVar[str] = "Win"
    LOSE: typing.ClassVar[str] = "Lose"
    DRAW: typing.ClassVar[str] = "Draw"

    opponent_input: str
    player_input: str
    opponent_input_map: dict
    player_input_map: dict
    base_points_map: dict
    result_points_map: dict

    def __post_init__(self):
        draw_result = (
            self.result_points_map[self.DRAW],
            self.result_points_map[self.DRAW],
        )
        player_win_result = (
            self.result_points_map[self.LOSE],
            self.result_points_map[self.WIN],
        )
        player_lose_result = (
            self.result_points_map[self.WIN],
            self.result_points_map[self.LOSE],
        )
        result_table = {
            (self.ROCK, self.ROCK): draw_result,
            (self.PAPER, self.PAPER): draw_result,
            (self.SCISSORS, self.SCISSORS): draw_result,
            (self.ROCK, self.SCISSORS): player_lose_result,
            (self.ROCK, self.PAPER): player_win_result,
            (self.PAPER, self.ROCK): player_lose_result,
            (self.PAPER, self.SCISSORS): player_win_result,
            (self.SCISSORS, self.PAPER): player_lose_result,
            (self.SCISSORS, self.ROCK): player_win_result,
        }

        opponent_choice = self.opponent_input_map[self.opponent_input]
        player_choice = self.player_input_map[self.player_input]
        base_score = (
            self.base_points_map[opponent_choice],
            self.base_points_map[player_choice],
        )
        result_score = result_table[(opponent_choice, player_choice)]
        self.opponent_score, self.player_score = tuple(
            sum(score) for score in zip(base_score, result_score)
        )


def parse_input_file(filename: str):
    current_dir = os.path.dirname(__file__)
    full_file_path = os.path.join(current_dir, filename)
    with open(full_file_path) as input_file:
        parsed_input = []
        for line in input_file.read().splitlines():
            parsed_input.append(
                tuple(line.split(" "))
            )
    return parsed_input


def rps_tournament(all_game_data):
    opponent_input_map = {
        "A": RPSGame.ROCK,
        "B": RPSGame.PAPER,
        "C": RPSGame.SCISSORS,
    }
    player_input_map = {
        "X": RPSGame.ROCK,
        "Y": RPSGame.PAPER,
        "Z": RPSGame.SCISSORS,
    }
    base_points_map = {
        RPSGame.ROCK: 1,
        RPSGame.PAPER: 2,
        RPSGame.SCISSORS: 3,
    }
    result_points_map = {
        RPSGame.WIN: 6,
        RPSGame.LOSE: 0,
        RPSGame.DRAW: 3
    }
    games = []
    for opponent_input, player_input in all_game_data:
        games.append(
            RPSGame(
                opponent_input=opponent_input,
                player_input=player_input,
                opponent_input_map=opponent_input_map,
                player_input_map=player_input_map,
                base_points_map=base_points_map,
                result_points_map=result_points_map,
            )
        )
    return sum([game.player_score for game in games])


def part_2_input_translator(original_game_data):
    a_remap = {
        "X": "Z",
        "Y": "X",
        "Z": "Y",
    }
    c_remap = {
        "X": "Y",
        "Y": "Z",
        "Z": "X",
    }

    translated_game_data = []
    for game in original_game_data:
        opponent, player = game
        if opponent == "B":
            translated_game_data.append(game)
        elif opponent == "A":
            translated_game_data.append(
                (opponent, a_remap[player])
            )
        elif opponent == "C":
            translated_game_data.append(
                (opponent, c_remap[player])
            )
    return translated_game_data


def main():
    parsed_input = parse_input_file("input.txt")

    part_1_result = rps_tournament(parsed_input)
    print(f"Part 1: {part_1_result}")

    part_2_data = part_2_input_translator(parsed_input)
    part_2_result = rps_tournament(part_2_data)
    print(f"Part 2: {part_2_result}")


if __name__ == "__main__":
    main()
