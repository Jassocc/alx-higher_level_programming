#!/usr/bin/python3
"""
Module 6
definition of square
"""


class Square:
    """
    Square definition
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        initilisation of square
        size of square and position of ints
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        retrieves size
        """
        ar = self.__size
        return ar

    @size.setter
    def size(self, value):
        """
        checks flags and returns errors
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """
        retrieves position
        """
        ars = self.__position
        return ars

    @position.setter
    def position(self, value):
        """
        checks flags and raises errors accordingly
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not isinstance(value[0], int) or not isinstance(value[1], int)
                or value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        returns current square
        """
        arse = self.__size ** 2
        return arse

    def my_print(self):
        """
        prints to stdout with #
        """
        if self.__size == 0:
            print()
        else:
            for row in range(self.__position[1]):
                print()
            for row in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
