#!/usr/bin/python3
"""
Module adds 2 integers and or floats together
A must be an int or float
B must be an int or float/ B has a default value of 98
"""
def add_integer(a, b=98):
    """
    add_integer should return a + b as integers although
    the values can be both ints and floats
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        return (int(a) + int(b))
