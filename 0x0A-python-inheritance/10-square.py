#!/usr/bin/python3
"""
Module 10-square

class square that inherits the rectangle class
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    new class that inherits attributes from rectangle
    """
    def __init__(self, size):
        """
        initializer of class
        """
        super().__init__(size, size)
        self.__size = size
        super().integer_validator("size", size)
