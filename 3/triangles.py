#!/usr/bin/env python
triangles = []
with open('input.txt', 'r') as input_file:
    for line in input_file:
        triangles.append(([int(side) for side in line.split()]))

new_triangles = []
for index in range(len(triangles) / 3):
    for offset in range(3):
        new_triangle = [triangles[(index * 3)][offset],
                        triangles[(index * 3) + 1][offset],
                        triangles[(index * 3) + 2][offset]]
        new_triangles.append(new_triangle)


def is_valid(triangle):
    side1 = (triangle[0] + triangle[1] > triangle[2])
    side2 = (triangle[0] + triangle[2] > triangle[1])
    side3 = (triangle[1] + triangle[2] > triangle[0])
    return all([side1, side2, side3])


def count_valid_triangles(triangles):
    valid_triangles = 0
    for triangle in triangles:
        if is_valid(triangle):
            valid_triangles += 1
    return valid_triangles

print "ANSWER 1: %s" % count_valid_triangles(triangles)
print "ANSWER 2: %s" % count_valid_triangles(new_triangles)
