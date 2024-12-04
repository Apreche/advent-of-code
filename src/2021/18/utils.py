
from typing import List


def add_to_rightmost_int(stack: List, x: int) -> List:
    """
    Add x to rightmost int in l
    if no int in l, do nothing
    return modified l
    """
    int_locations = [isinstance(i, int) for i in stack]
    if not any(int_locations):
        return stack
    int_locations.reverse()
    last_index = len(int_locations) - 1 - int_locations.index(True)
    stack[last_index] += x
    return stack


def add_to_leftmost_int(stack: List, x: int) -> List:
    """
    Add x to leftmost int in l
    if no int in l, do nothing
    return modified l
    """
    int_locations = [isinstance(i, int) for i in stack]
    if not any(int_locations):
        return stack
    index = int_locations.index(True)
    stack[index] += x
    return stack
