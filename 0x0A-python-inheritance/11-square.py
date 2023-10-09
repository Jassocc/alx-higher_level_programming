#!/usr/bin/python3
"""
Moduloe 11-Square

Class Square that has its own attributes
and inherits attributes from the Rectangle class
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    sqiare class with attributes
    inherited from rectangle
    """
    def __init__(self, size):
        """
        initializer of class
        """
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """
        string displayer
        """
        res = "[Square] {:d}/{:d}".format(self.__size, self.__size)
        return res
