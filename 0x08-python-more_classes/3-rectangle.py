#!/usr/bin/python3
"""
Module 3-rectangle
defines the class rectangle and returns the are
"""


class Rectangle:
    """
    definition of rectangle with a few attributes
    attributes include: width height, perimeter, area
    """
    def __init__(self, width=0, height=0):
        """
        initialize rectangle
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

    def area(self):
        """
        returns the area of the rectangle
        """
        result = self.__height * self.__width
        return result

    def perimeter(self):
        """
        returns the primeter of the rectangle
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        res = 2 * (self.__height + self.__width)
        return res

    def __str__(self):
        """
        prints the #'s
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        vals = "\n".join(["#" * self.__width for ro in range(self.__height)])
        return vals
