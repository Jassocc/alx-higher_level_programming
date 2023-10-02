#!/usr/bin/python3
"""
module-4 definition of class rectangle
attributes: width, height, area, perimeter
"""


class Rectangle:
    """
    defdinition of rectangle class
    """
    def __init__(self, width=0, height=0):
        """
        initializer of rectangle
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        retrieves width
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
        returns the area of rectangle
        """
        res = self.__width * self.__height
        return res

    def perimeter(self):
        """
        returns the perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        result = 2 * (self.__width + self.__height)
        return result

    def __str__(self):
        """
        prints the #'s
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        vals = "\n".join(["#" * self.__width for row in range(self.__height)])
        return vals

    def __repr__(self):
        """
        string rep for newer instances
        """
        rec_result = "Rectangle({:d}, {:d})".format(self.width, self.height)
        return rec_result
