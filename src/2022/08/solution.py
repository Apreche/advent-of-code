#!/usr/bin/env python

import math
import os


def parse_input_file(filename: str):
    current_dir = os.path.dirname(__file__)
    full_file_path = os.path.join(current_dir, filename)
    with open(full_file_path) as input_file:
        grid = []
        for line in input_file.read().splitlines():
            row = [int(n) for n in line]
            grid.append(row)
    return grid


def is_visible(grid, x, y):
    height = len(grid)
    width = len(grid[0])
    if (x in [0, width]) or (y in [0, height]):
        return True
    target_height = grid[y][x]

    row = grid[y]
    left_blockers = [t for t in row[:x] if t >= target_height]
    if not left_blockers:
        return True
    right_blockers = [t for t in row[x+1:] if t >= target_height]
    if not right_blockers:
        return True

    column = [grid[cy][x] for cy in range(0, height)]
    top_blockers = [t for t in column[:y] if t >= target_height]
    if not top_blockers:
        return True
    bottom_blockers = [t for t in column[y+1:] if t >= target_height]
    if not bottom_blockers:
        return True

    return False


def scenic_score(grid, x, y):
    height = len(grid)
    width = len(grid[0])
    if (x in [0, width]) or (y in [0, height]):
        return 0
    target_height = grid[y][x]

    row = grid[y]
    left_trees = [t for t in row[:x]]
    left_trees.reverse()
    right_trees = [t for t in row[x+1:]]
    column = [grid[cy][x] for cy in range(0, height)]
    top_trees = [t for t in column[:y]]
    top_trees.reverse()
    bottom_trees = [t for t in column[y+1:]]
    lines_of_sight = [
        left_trees,
        right_trees,
        top_trees,
        bottom_trees,
    ]
    scores = []
    for line in lines_of_sight:
        score = 0
        for tree in line:
            score += 1
            if tree >= target_height:
                break
        scores.append(score)
    return math.prod(scores)


def best_scenic_score(grid):
    scenic_scores = []
    height = len(grid)
    width = len(grid[0])
    for x in range(1, width - 1):
        for y in range(1, height - 1):
            score = scenic_score(grid, x, y)
            scenic_scores.append(score)
    return max(scenic_scores)


def count_visible(grid):
    height = len(grid)
    width = len(grid[0])
    num_visible = (height * 2) + (width * 2) - 4
    for x in range(1, width - 1):
        for y in range(1, height - 1):
            if is_visible(grid, x, y):
                num_visible += 1
    return num_visible


def main():
    grid = parse_input_file("input.txt")

    part_1_result = count_visible(grid)
    print(f"Part 1: {part_1_result}")

    part_2_result = best_scenic_score(grid)
    print(f"Part 2: {part_2_result}")


if __name__ == "__main__":
    main()
