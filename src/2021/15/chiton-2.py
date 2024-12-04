#!/usr/bin/env python

import heapq
import math
import os


def wrap_nine(num):
    while num > 9:
        num = num - 9
    return num


def multiply_grid(grid, factor=5):
    new_grid = []
    for fy in range(factor):
        for row in grid:
            new_row = []
            for fx in range(factor):
                for column in row:
                    new_row.append(
                        wrap_nine(column + fx + fy)
                    )
            new_grid.append(new_row)
    return new_grid


class DiGraph:
    def __init__(self, int_nodes):
        self.height = None
        self.width = None
        self.graph = self._process_int_nodes(int_nodes)

    def _process_int_nodes(self, int_nodes):
        graph = {}
        self.height = len(int_nodes)
        for y_index, row in enumerate(int_nodes):
            if self.width is None:
                self.width = len(row)
            for x_index, column in enumerate(row):
                node = []
                for dest_x, dest_y in self._get_adjacencies(
                    x_index, y_index, self.width, self.height
                ):
                    node.append(
                        ((dest_x, dest_y), int_nodes[dest_y][dest_x])
                    )
                graph[(x_index, y_index)] = node
        return graph

    def _get_adjacencies(self, x, y, width, height):
        coords = []
        for xd in [-1, 1]:
            fx = x + xd
            xgood = (fx >= 0) and (fx < width)
            if xgood:
                coords.append((fx, y))
        for yd in [-1, 1]:
            fy = y + yd
            ygood = (fy >= 0) and (fy < height)
            if ygood:
                coords.append((x, fy))
        return coords

    def _heuristic(self, coord, end):
        x1, y1 = coord
        x2, y2 = end
        return math.hypot(
            x2 - x1, y2 - y1
        )

    def shortest_path(self, start=(0, 0), end=None):
        if end is None:
            end = (self.width - 1, self.height - 1)

        open_list = []
        heapq.heappush(open_list, (0, start))
        f_values = {}
        f_values[start] = 0
        adj_map = {start: start}

        while open_list:
            current_node = heapq.heappop(open_list)[1]
            current_f = f_values[current_node]

            if current_node == end:
                shortest_path = []
                while adj_map[current_node] != current_node:
                    shortest_path.append(current_node)
                    current_node = adj_map[current_node]
                shortest_path.append(start)
                shortest_path.reverse()
                return(shortest_path, current_f)

            for neighbor, cost in self.graph[current_node]:
                new_f = current_f + cost
                if (neighbor not in f_values) or (new_f < f_values[neighbor]):
                    f_values[neighbor] = new_f
                    priority = new_f + self._heuristic(neighbor, end)
                    heapq.heappush(open_list, (priority, neighbor))
                    adj_map[neighbor] = current_node


def parse_input_file(filename: str):
    current_dir = os.path.dirname(__file__)
    full_file_path = os.path.join(current_dir, filename)
    with open(full_file_path) as input_file:
        parsed_input = []
        for line in input_file.read().splitlines():
            parsed_input.append([int(x) for x in line])
    return parsed_input


def main():
    part_1_input = parse_input_file("input.txt")
    part_1_graph = DiGraph(part_1_input)
    part_1_path, part_1_cost = part_1_graph.shortest_path()

    part_1_result = part_1_cost
    print(f"Part 1: {part_1_result}")

    part_2_input = multiply_grid(part_1_input)
    part_2_graph = DiGraph(part_2_input)
    part_2_path, part_2_cost = part_2_graph.shortest_path()

    part_2_result = part_2_cost
    print(f"Part 2: {part_2_result}")


if __name__ == "__main__":
    main()
