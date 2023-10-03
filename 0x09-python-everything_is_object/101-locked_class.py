#!/usr/bin/python3
"""
defines Locked class which is a no class
no object attributes and prevents users from creaing instances
Except if the instance is called first_name
"""


class LockedClass():
    """
    definitions of locked class
    no attributes or functions
    """
    __slots__ = ("first_name")
