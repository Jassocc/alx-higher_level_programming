#!/usr/bin/python3
"""
Module 9-Student
class that identifies students with attributes
first name laste name and age
"""


class Student():
    """
    definitionb of class with attributes
    """
    def __init__(self, first_name, last_name, age):
        """
        initializer of class
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        public method
        """
        f_name = self.first_name
        l_name = self.last_name
        age = self.age
        return {
                "first_name": f_name,
                "last_name": l_name,
                "age": age}
