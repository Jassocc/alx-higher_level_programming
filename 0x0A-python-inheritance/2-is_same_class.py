#!/usr/bin/python3
"""
Module 2-is_same_class

returns true if object is a match to inxtance of class
"""


def is_same_class(obj, a_class):
    """
    checks if the class is the same
    """
    a = type(obj)
    return a == a_class
