#!/usr/bin/python3
"""
Module 3 print square
print a square with given number
function prototype:
    def print_square(size)
"""


def print_square(size):
    """
    prints square with the # and
    given number
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for a in range(size):
        print("#" * size)
