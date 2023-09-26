#!/usr/bin/python3
"""
Module 10
define maguic class
"""
import math

class MagicClass:
    """
    definition of MAgic Class
    """
    def __init__(self, radius=0):
        """
        initilisation of magic class
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """
        gives area
        """
        ar = (self.__radius ** 2) * math.pi
        return ar

    def circumference(self):
        """
        calculate circumference
        """
        ars = 2 * math.pi * self.__radius
        return ars
