#!/usr/bin/python3
"""
Module 8- define class rectangle
along with all its functions and attributes
"""


class Rectangle:
    """
    definition of class Rectangle along all attributes and functions
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
        if self.__height == 0 or self.__width == 0:
            return 0
        result = 2 * (self.__height + self.__width)
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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        returns biggest rectagle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2
