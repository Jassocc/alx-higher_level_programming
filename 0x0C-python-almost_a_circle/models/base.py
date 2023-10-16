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

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes he json string rep to a file
        """
        filename = cls.__name__ + ".json"
        obj_dict = []
        if list_objs is not None:
            for obj in list_objs:
                obj_dict.append(obj.to_dictionary())
        with open(filename, mode='w', encoding='UTF-8') as file:
            file.write(cls.to_json_string(obj_dict))
