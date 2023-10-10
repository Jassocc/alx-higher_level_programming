#!/usr/bin/python3
"""
Module 4-from_json_string
Returns a string from the json
"""
import json


def from_json_string(my_str):
    """
    Returns an object from the json
    """
    res = json.loads(my_str)
    return res
