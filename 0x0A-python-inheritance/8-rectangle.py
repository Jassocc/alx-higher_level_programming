#!/usr/bin/python3
"""
Module 8-Rectangle

Rectangle is a classs that inherits properties from BaseGeometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    class with its own properties and inherited properties
    """
    def __init__(self, width, height):
        """
        initializer of rectangle
        """
        self.__height = height
        self.__width = width
        super().integer_validator("width", width)
        super().integer_validator("height", height)
