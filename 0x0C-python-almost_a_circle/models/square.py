#!/usr/bin/python3
from models.rectangle import Rectangle
"""
class Square
inherits from The Rectangle class 
also has its own attributes
"""


class Square(Rectangle):
    """
    class definition with inheritance
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        initializer of class
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        gets the size
        """
        res = self.width
        return res

    @size.setter
    def size(self, value):
        """
        sets the size
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        returns string rep of square
        """
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(
                self.id, self.x, self.y, self.size)

