#!/usr/bin/env python

import os


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

    def shortest_path(self, start=(0, 0), end=None):
        if end is None:
            end = (self.width - 1, self.height - 1)

        open_list = set([start])
        closed_list = set()
        f_values = {}
        f_values[start] = 0
        adj_map = {start: start}

        while len(open_list) > 0:
            current_node = min(
                {coord: f for coord, f in f_values.items() if coord in open_list},
                key=f_values.get
            )
            current_f = f_values.get(current_node)

            if current_node == end:
                shortest_path = []
                while adj_map[current_node] != current_node:
                    shortest_path.append(current_node)
                    current_node = adj_map[current_node]
                shortest_path.append(start)
                shortest_path.reverse()
                return(shortest_path, current_f)

            for neighbor, cost in self.graph[current_node]:
                if (neighbor not in open_list) and (neighbor not in closed_list):
                    open_list.add(neighbor)
                    adj_map[neighbor] = current_node
                    f_values[neighbor] = current_f + cost
                else:
                    if f_values[neighbor] > current_f + cost:
                        f_values[neighbor] = current_f + cost
                        adj_map[neighbor] = current_node

                        if neighbor in closed_list:
                            closed_list.remove(neighbor)
                            open_list.add(neighbor)

            open_list.remove(current_node)
            closed_list.add(current_node)


def parse_input_file(filename: str):
    current_dir = os.path.dirname(__file__)
    full_file_path = os.path.join(current_dir, filename)
    with open(full_file_path) as input_file:
        parsed_input = []
        for line in input_file.read().splitlines():
            parsed_input.append([int(x) for x in line])
    return parsed_input


def main():
    parsed_input = parse_input_file("input.txt")
    graph = DiGraph(parsed_input)
    path, cost = graph.shortest_path()

    part_1_result = cost
    print(f"Part 1: {part_1_result}")

    part_2_result = None
    print(f"Part 2: {part_2_result}")


if __name__ == "__main__":
    main()
