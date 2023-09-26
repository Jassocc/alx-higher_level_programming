#!/usr/bin/python3
"""
Module 2
defines a square
"""


class Square:
    """
    Definition of a square
    """
    def __init__(self, size=0):
        """
        initialisation of square
        size of square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
