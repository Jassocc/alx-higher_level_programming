#!/usr/bin/python3
"""
Module 9
defines square
"""


class Square:
    """
    definitions of square
    """
    def __init__(self, size=0):
        """
        initialize square
        """
        self.size = size

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
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        returns area of swaure
        """
        ars = self.__size ** 2
        return ars

    def __lt__(self, x):
        """
        smaller than <
        """
        a = self.area() < x.area()
        return a

    def __le__(self, x):
        """
        smaller or equal to <=
        """
        b = self.area() <= x.area()
        return b

    def __eq__(self, x):
        """
        equal ==
        """
        c = self.area() == x.area()
        return c

    def __ne__(self, x):
        """
        not equal !=
        """
        d = self.area() != x.area()
        return d

    def __gt__(self, x):
        """
        greater than >
        """
        e = self.area() > x.area()
        return e

    def __ge__(self, x):
        """
        greater than or eqal >=
        """
        f = self.area() >= x.area()
        return f
