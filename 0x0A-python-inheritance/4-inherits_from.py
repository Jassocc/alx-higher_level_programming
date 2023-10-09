#!/usr/bin/python3
"""
Module 4-inherits_from

returns true if object is instance of inherited class
false if otherwise
"""


def inherits_from(obj, a_class):
    """
    checks if object is instance of class
    """
    a = issubclass(type(obj), a_class)
    b = type(obj) is not a_class
    return a and b
