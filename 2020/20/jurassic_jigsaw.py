#!/usr/bin/env python

import math


TILE_SIZE = 10


def parse_input_file(filename: str):

    with open(filename) as input_file:
        all_tiles = {}
        current_tile = []
        for line in input_file.read().splitlines():
            if line == '':
                tile_id = int(current_tile[0][5:-1])
                all_tiles[tile_id] = {
                    "raw_data": current_tile[1:]
                }
                current_tile = []
            else:
                current_tile.append(line)
    return all_tiles


def hash_str_to_2bin(hash_string):
    new_string = hash_string.replace(
        '#', '1'
    ).replace(
        '.', '0'
    )
    reverse_string = new_string[::-1]
    int1 = int(new_string, 2)
    int2 = int(reverse_string, 2)
    pair = sorted([int1, int2])
    return tuple(pair)


def process_edges(tileset):
    for tile_id, tile in tileset.items():
        raw_top = tile['raw_data'][0]
        raw_bottom = tile['raw_data'][TILE_SIZE - 1]
        raw_left = ''.join(
            [t[0] for t in tile['raw_data']]
        )
        raw_right = ''.join(
            [t[TILE_SIZE - 1] for t in tile['raw_data']]
        )
        raw_edges = [
            raw_top,
            raw_bottom,
            raw_left,
            raw_right
        ]
        tileset[tile_id]['edges'] = [
            hash_str_to_2bin(e) for e in raw_edges
        ]
    return tileset


def count_edges(tileset_with_edges):
    edge_counts = {}
    for tile_id, tile in tileset_with_edges.items():
        for edge in tile['edges']:
            edge_counts.setdefault(edge, [])
            edge_counts[edge].append(tile_id)
    return edge_counts


def count_lone_edges_per_tile(edge_counts):
    tiles = {}
    for edge, tile_ids in edge_counts.items():
        if len(tile_ids) == 1:
            tiles.setdefault(tile_ids[0], 0)
            tiles[tile_ids[0]] += 1
    return tiles


def part_one_solution(lone_edge_count):
    corner_tiles = [x for x, y in lone_edge_count.items() if y == 2]
    return math.prod(corner_tiles)


def main():
    all_tiles = parse_input_file("input.txt")
    tileset_with_edges = process_edges(all_tiles)
    edge_counts = count_edges(tileset_with_edges)
    lone_edge_count = count_lone_edges_per_tile(
        edge_counts
    )

    part_1_result = part_one_solution(lone_edge_count)
    print(f"Part 1: {part_1_result}")

    part_2_result = None
    print(f"Part 2: {part_2_result}")


if __name__ == "__main__":
    main()
