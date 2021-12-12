#!/usr/bin/env python

import collections
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

    def _path_has_no_double_lower_visit(self, path):
        lowers_in_path = [node for node in path if node.islower()]

        # Alternative
        # lowers_in_path_set = set(lowers_in_path)
        # if len(lowers_in_path_set) < len(lowers_in_path):
        #     return False

        counter = collections.Counter(lowers_in_path)
        if max(counter.values()) == 2:
            return False
        return True

    def _can_visit(self, node, path):
        if node not in path:
            return True
        elif node.isupper():
            return True
        elif (node in ["start", "end"]):
            return node not in path
        else:
            return self._path_has_no_double_lower_visit(path)

    def find_all_part_2_paths(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if start not in self.graph:
            return []
        paths = []
        for node in self.graph[start]:
            if self._can_visit(node, path):
                newpaths = self.find_all_part_2_paths(node, end, path)
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

    part_2_paths = cave_graph.find_all_part_2_paths("start", "end")
    part_2_result = len(part_2_paths)
    print(f"Part 2: {part_2_result}")


if __name__ == "__main__":
    main()
