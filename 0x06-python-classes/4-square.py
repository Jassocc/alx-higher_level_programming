#!/usr/bin/python3
"""
Module 4
getter and setter additions
"""


class Square:
    """
    definition of square
    """
    def __init__(self, size=0):
        """
        initialisation of square original size 0
        """
        self.size = size

    @property
    def size(self):
        """
        getter for the size
        """
        si = self.__size
        return si

    @size.setter
    def size(self, value):
        """
        sets the size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size mus tbe >= 0")
        else:
            self.__size = value

    def area(self):
        """
        area of the square esentially size ** 2
        """
        area_results = self.__size ** 2
        return area_results
