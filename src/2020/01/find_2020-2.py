#!/usr/bin/env python
import itertools
from typing import List


def file_to_int_list(filename: str) -> List[int]:
    # Convert a text file with one integer per line to a list of integers
    numbers = []
    with open(filename) as input_file:
        numbers = [int(line) for line in input_file.read().splitlines()]
    return numbers


def find_sum_get_product(query_sum: int, values: List[int]) -> int:
    # Take a list of integers and find the pairing with the specified sum
    # return the product of the two integers in the pair
    # Pairs with identical sums clobber each other
    all_sums = {
        (x + y + z): (x, y, z) for x, y, z in itertools.product(
            values, values, values
        ) if ((x != y) and (x != z) and (y != z))
    }
    a, b, c = all_sums[query_sum]
    return a * b * c


if __name__ == '__main__':
    values = file_to_int_list('input.txt')
    result = find_sum_get_product(2020, values)
    print(result)
