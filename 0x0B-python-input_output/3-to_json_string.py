#!/usr/bin/python3
"""
Module 3-Json
Json representation of a string
"""
import json


def to_json_string(my_obj):
    """
    returns Json rep of a string
    """
    res = json.dumps(my_obj)
    return res
