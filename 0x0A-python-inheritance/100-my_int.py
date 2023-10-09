#!/usr/bin/python3
"""
Module 11-My_int

class that inherits from int
"""


class MyInt(int):
    """
    MyInt inherits from int
    """
    def __init__(self, digit):
        """
        initializer for class
        """
        self.digit = digit

    def __eq__(self, other):
        """
        equality checker
        """
        a = super().__ne__(other)
        return a

    def __ne__(self, other):
        """"
        not equal
        """
        b = super().__eq__(other)
        return b
