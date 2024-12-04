#!/usr/bin/env python

import os


class Board:
    def __init__(self, grid=[]):
        self.grid = grid
        self.marks = []

    def _is_winner(self):
        if len(self.marks) < 5:
            return False

        for row in range(5):
            if (len([mark for mark in self.marks if mark[0] == row])) == 5:
                return True
            if (len([mark for mark in self.marks if mark[1] == row])) == 5:
                return True

    def _mark_digit(self, digit):
        for x in range(5):
            for y in range(5):
                if self.grid[x][y] == digit:
                    self.marks.append((x, y))

    def _get_score(self, winning_ball):
        unmarked_sum = 0
        for x in range(5):
            for y in range(5):
                if (x, y) not in self.marks:
                    unmarked_sum += self.grid[x][y]
        return unmarked_sum * winning_ball

    def check_all_balls(self, balls):
        for index, ball in enumerate(balls):
            self._mark_digit(ball)
            if self._is_winner():
                return index, self._get_score(ball)


def score_all_boards(balls, boards):
    board_scores = []
    for board_index, board in enumerate(boards):
        winning_index, score = board.check_all_balls(balls)
        board_scores.append((board_index, winning_index, score))
    return board_scores


def find_winning_board(board_scores):
    current_winner = None
    current_winning_index = 1000
    for board_index, winning_index, score in board_scores:
        if winning_index < current_winning_index:
            current_winner = (board_index, winning_index, score)
            current_winning_index = winning_index
    return current_winner


def find_losing_board(board_scores):
    current_loser = None
    current_losing_index = 0
    for board_index, winning_index, score in board_scores:
        if winning_index > current_losing_index:
            current_loser = (board_index, winning_index, score)
            current_losing_index = winning_index
    return current_loser


def parse_input_file(filename: str):
    current_dir = os.path.dirname(__file__)
    full_file_path = os.path.join(current_dir, filename)
    with open(full_file_path) as input_file:
        balls = [int(x) for x in input_file.readline().strip().split(',')]
        boards = []
        current_board = []
        for line in input_file.read().splitlines():
            if line in ["\n", '']:
                if current_board != []:
                    boards.append(Board(current_board))
                    current_board = []
            else:
                row = [int(x) for x in line.strip().split()]
                current_board.append(row)
        boards.append(Board(current_board))
    return balls, boards


def main():
    balls, boards = parse_input_file("input.txt")
    board_scores = score_all_boards(balls, boards)
    board, index, score = find_winning_board(board_scores)

    part_1_result = score
    print(f"Part 1: {part_1_result}")

    board, index, score = find_losing_board(board_scores)
    part_2_result = score
    print(f"Part 2: {part_2_result}")


if __name__ == "__main__":
    main()
