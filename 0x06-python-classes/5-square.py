#!/usr/bin/python3
"""
Module 3
Defines Class square
"""


class Square:
    """
    class square definition
    """
    def __init__(self, size=0):
        """
        Initiliasation of square
        """
        self.size = size

    @property
    def size(self):
        """
        retrieves current size
        """
        ar = self.__size
        return ar

    @size.setter
    def size(self, value):
        """
        raises all errors
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        returns current square area
        """
        arr = self.__size ** 2
        return arr

    def my_print(self):
        """
        prints with # to stdout
        """
        if self.__size == 0:
            print()
        else:
            for row in range(self.__size):
                print("#" * self.__size)
