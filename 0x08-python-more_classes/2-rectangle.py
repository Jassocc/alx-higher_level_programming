#!/usr/bin/python3
"""
Module 2-Rectangle.py
defines a class Rectangle
"""


class Rectangle:
    """
    Rectangle class with attributes:
    width, height, perimeter and area
    """
    def __init__(self, width=0, height=0):
        """
        initializes the rectangle class
        """
        self.__width = width
        self.__height = height

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
        retrieves height
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

    def area(self):
        """
        returns area of rectangle
        """
        result = self.__width * self.__height
        return result

    def perimeter(self):
        """
        returns the perimeter of rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        result = 2 * (self.__width + self.__height)
        return result
