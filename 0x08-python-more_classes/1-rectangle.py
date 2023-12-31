#!/usr/bin/python3
"""
Module 1- defines
a rectangle
"""


class Rectangle:
    """
    defines a rectangle that gets retrieved and setted
    there are 2 attributes, width and height
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        retrieves the width
        """
        wi = self.__width
        return wi

    @width.setter
    def width(self, value):
        """
        sets the width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        retrieves the height
        """
        he = self.__height
        return he

    @height.setter
    def height(self, value):
        """
        sets the height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
