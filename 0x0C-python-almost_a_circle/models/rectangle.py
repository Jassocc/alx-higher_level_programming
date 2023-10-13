#!/usr/bin/python3
"""
Rectangle class that inherits from the base class
It also has its own attributes which
are mostly private
"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class with inheritance
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        initializer of class
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        getter for width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        sets the width
        """
        self.__width = value

    @property
    def height(self):
        """
        getter for height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        sets the height
        """
        self.__height = value

    @property
    def x(self):
        """
        getter for x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        sets the x
        """
        self.__x = value

    @property
    def y(self):
        """
        getter for y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        sets the y
        """
        self.__y = value
