#!/usr/bin/python3
"""
Module 9-Rectangle class

class has its own properties and inherits from BaseGeometry
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Class with its own properties and properties
    thats inhereted from parent class
    """
    def __init__(self, width, height):
        """
        initializer of class
        """
        self.__height = height
        self.__width = width
        super().integer_validator("height", height)
        super().integer_validator("width", width)

    def area(self):
        """
        area of rectangle
        """
        Result = self.__height * self.__width
        return Result

    def __str__(self):
        """
        string display
        """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
