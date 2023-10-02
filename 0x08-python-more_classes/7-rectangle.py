#!/usr/bin/python3
"""
Module 7- define class rectangle
with all of the attributes
"""


class Rectangle:
    """
    definition of the class rectangle with all attributes
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        initializes the class rectangle
        """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

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
        returns the area
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
        prints with #'s
        """
        if self.__height == 0 or self.__width == 0:
            return ""
        vals = "\n".join([str(self.print_symbol) * self.__width
                         for rom in range(self.__height)])
        return vals

    def __repr__(self):
        """
        string rep for newer instance
        """
        rec_res = "Rectangle({:d}, {:d})".format(self.__width, self.__height)
        return rec_res

    def __del__(self):
        """
        deletes instance of class
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
