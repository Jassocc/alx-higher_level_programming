#!/usr/bin/python3
"""
Module 8-class_to+_json
returns the dictionary description with
simple data structure list
"""


def class_to_json(obj):
    """
    returns description with structure list
    """
    result = obj.__dict__
    return result
