#!/usr/bin/python3
"""
Module 3
find the area of a square
"""


class Square:
    """
    definition of square
    size is the len of square sides
    """
    def __init__(self, size=0):
        """
        initialisation of square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        area of the square essentially ** 2
        """
        area_results = self.__size ** 2
        return area_results
