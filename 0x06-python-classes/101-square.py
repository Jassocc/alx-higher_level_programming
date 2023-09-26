#!/usr/bin/python3
"""
Module 8
defines square
"""


class Square:
    """
    definition of square
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        initilisation of square
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
        sets size
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

    @position.setter
    def position(self, value):
        """
        sets position
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not isinstance(value[0], int) or not isinstance(value[1], int)
                or value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integer")
        else:
            self.__position = value

    def area(self):
        """
        returns the square area
        """
        arb = self.__size ** 2
        return arb

    def my_print(self):
        """
        prints to stdout with #
        """
        if self.__size == 0:
            print()
            return
        for arr in range(self.__position[1]):
            print()
        for arr in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """
        string representation of square
        """
        if self.__size == 0:
            return ""
        result = "\n" * self.__position[1]
        result += "\n".join(" " * self.__position[0] + "#" * self.__size
                            for arr in range(self.__size))
        return result
