#!/usr/bin/python3
"""
Module 7-area, integer_validator

area raises exception and validator checks for special instances
"""


class BaseGeometry:
    """
    class that has 2 functions for attributes
    """
    def area(self):
        """
        raises an exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validates value
        """
        if not isinstance(value, int):
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
