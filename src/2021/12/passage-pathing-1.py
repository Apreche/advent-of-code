#!/usr/bin/env python

import os


class CaveGraph:
    def __init__(self, links):
        self._build_graph(links)

    def _add_link(self, link):
        nodea, nodeb = link
        self.graph.setdefault(nodea, set())
        self.graph.setdefault(nodeb, set())
        self.graph[nodea].add(nodeb)
        self.graph[nodeb].add(nodea)

    def _build_graph(self, links):
        self.graph = {}
        for link in links:
            self._add_link(link)

    def find_all_paths(self, start, end, path=[]):
        # Thanks https://www.python.org/doc/essays/graphs/
        path = path + [start]
        if start == end:
            return [path]
        if start not in self.graph:
            return []
        paths = []
        for node in self.graph[start]:
            if (node not in path) or (node.isupper()):
                newpaths = self.find_all_paths(node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths


def parse_input_file(filename: str):
    current_dir = os.path.dirname(__file__)
    full_file_path = os.path.join(current_dir, filename)
    with open(full_file_path) as input_file:
        parsed_input = []
        for line in input_file.read().splitlines():
            parsed_input.append(tuple(line.split('-')))
    return parsed_input


def main():
    parsed_input = parse_input_file("input.txt")
    cave_graph = CaveGraph(parsed_input)
    paths = cave_graph.find_all_paths("start", "end")

    part_1_result = len(paths)
    print(f"Part 1: {part_1_result}")

    part_2_result = None
    print(f"Part 2: {part_2_result}")


if __name__ == "__main__":
    main()
