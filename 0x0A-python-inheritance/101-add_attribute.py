#!/usr/bin/python3
"""
Module 12

Adds a new attribute to an object when possible
"""


def add_attribute(obj, attr, val):
    """
    functipon to add attribute to object
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, attr, val)
