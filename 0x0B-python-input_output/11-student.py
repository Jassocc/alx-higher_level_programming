#!/usr/bin/python3
"""
Module 11-student
definition of class student along with attributes
like first name, last name and age
"""


class Student():
    """
    definition of class student
    """
    def __init__(self, first_name, last_name, age):
        """
        initializer of class
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieves dictionary rep
        """
        if attrs is not None:
            json_data = {}
            for attr in attrs:
                if hasattr(self, attr):
                    json_data[attr] = getattr(self, attr)
            return json_data
        return self.__dict__

    def reload_from_json(self, json):
        """
        replaces attrs of student
        """
        for key, value in json.items():
            setattr(self, key, value)
