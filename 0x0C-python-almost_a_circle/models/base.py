#!/usr/bin/python3
import json
"""
Classs known as base with different
Attributes and a class constructor
"""


class Base:
    """
    class definition
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        initiaizer of class
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns json string to rep of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
