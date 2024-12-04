#!/usr/bin/env python

import os


class FileSystem:
    def __init__(self):
        self.filesystem = {}
        self.pwd_path = []
        self.pwd = self.filesystem

    def cd(self, param):
        if param == "/":
            self.pwd_path = []
        elif param == "..":
            self.pwd_path.pop()
        else:
            self.pwd_path.append(param)

        self.pwd = self.filesystem
        for dir in self.pwd_path:
            self.pwd = self.pwd[dir]

    def ls(self):
        for filename, contents in self.pwd.items():
            if isinstance(contents, dict):
                print(f"{filename} (dir)")
            else:
                print(f"{filename} ({contents})")

    def mkdir(self, dirname):
        self.pwd.setdefault(dirname, {})

    def touch(self, filename, filesize):
        self.pwd[filename] = filesize

    @property
    def dirsize(self):
        sizes = []
        for filename, file in self.pwd.items():
            if isinstance(file, int):
                sizes.append(file)
            else:
                self.cd(filename)
                sizes.append(self.dirsize)
                self.cd("..")
        return sum(sizes)

    def sum_limited_dir_sizes(self, min_limit=0, max_limit=100000):
        total_sizes = []
        limited_sizes = []
        for filename, file in self.pwd.items():
            if isinstance(file, int):
                total_sizes.append(file)
            else:
                self.cd(filename)
                inside_total_sizes, inside_limited_sizes = self.sum_limited_dir_sizes(
                    max_limit=max_limit,
                    min_limit=min_limit,
                )
                total_sizes.append(inside_total_sizes)
                limited_sizes += inside_limited_sizes
                self.cd("..")
        current_dir_total_size = sum(total_sizes)
        if current_dir_total_size >= min_limit and current_dir_total_size <= max_limit:
            limited_sizes.append(current_dir_total_size)
        return current_dir_total_size, limited_sizes


def find_deletable_directory(filesystem):
    filesystem.cd("/")
    total_disk_space = 70000000
    required_free_space = 30000000
    used_space = filesystem.dirsize
    current_free_space = total_disk_space - used_space
    space_to_free = required_free_space - current_free_space
    filesystem.cd("/")
    _, potential_dir_sizes_to_delete = filesystem.sum_limited_dir_sizes(
        min_limit=space_to_free,
        max_limit=used_space,
    )
    return min(potential_dir_sizes_to_delete)


def create_filesystem(command_input):
    filesystem = FileSystem()
    for raw_command in command_input:
        command = raw_command.split(" ")
        if command[0] == "$" and command[1] == "cd":
            filesystem.cd(command[2])
        if command[0] != "$":
            if command[0] == "dir":
                filesystem.mkdir(command[1])
            else:
                filesystem.touch(command[1], int(command[0]))
    filesystem.cd("/")
    return filesystem


def parse_input_file(filename: str):
    current_dir = os.path.dirname(__file__)
    full_file_path = os.path.join(current_dir, filename)
    with open(full_file_path) as input_file:
        parsed_input = []
        for line in input_file.read().splitlines():
            parsed_input.append(line)
    return parsed_input


def main():
    parsed_input = parse_input_file("input.txt")
    filesystem = create_filesystem(parsed_input)
    _, limited_sizes = filesystem.sum_limited_dir_sizes(
        max_limit=100000
    )

    part_1_result = sum(limited_sizes)
    print(f"Part 1: {part_1_result}")

    filesystem.cd("/")
    part_2_result = find_deletable_directory(filesystem)
    print(f"Part 2: {part_2_result}")


if __name__ == "__main__":
    main()
