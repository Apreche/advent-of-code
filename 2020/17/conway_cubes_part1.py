#!/usr/bin/env python

def parse_input_file(filename: str):

    with open(filename) as input_file:

        space = {}
        for row, line in enumerate(
            input_file.read().splitlines()
        ):
            for column, value in enumerate(line):
                if value == '#':
                    space[(column, row, 0)] = True
    return space


def edges_of_space(space):
    xs = []
    ys = []
    zs = []

    for x, y, z in space.keys():
        xs.append(x)
        ys.append(y)
        zs.append(z)

    edges = {
        'minx': min(xs),
        'maxx': max(xs),
        'miny': min(ys),
        'maxy': max(ys),
        'minz': min(zs),
        'maxz': max(zs),
    }
    return edges


def active_neighbor_count(space, coordinate):
    active_neighbors = 0
    x, y, z = coordinate
    for xt in range(x-1, x+2):
        for yt in range(y-1, y+2):
            for zt in range(z-1, z+2):
                neighbor_coord = (xt, yt, zt)
                if neighbor_coord != coordinate:
                    neighbor = space.get(
                        neighbor_coord, False
                    )
                    if neighbor:
                        active_neighbors += 1
    return active_neighbors


def conway_cycle(space):
    edge = edges_of_space(space)
    new_space = {}
    for x in range(edge['minx'] - 1, edge['maxx'] + 2):
        for y in range(edge['miny'] - 1, edge['maxy'] + 2):
            for z in range(edge['minz'] - 1, edge['maxz'] + 2):
                coordinate = (x, y, z)
                current = space.get(coordinate, False)
                count = active_neighbor_count(
                    space, coordinate
                )
                if current:
                    if 2 <= count <= 3:
                        new_space[coordinate] = True
                else:  # not already active
                    if count == 3:
                        new_space[coordinate] = True
    return new_space


def main():
    space = parse_input_file("input.txt")
    for i in range(6):
        space = conway_cycle(space)

    part_1_result = len(space)
    print(f"Part 1: {part_1_result}")


if __name__ == "__main__":
    main()
