#!/usr/bin/python3
"""
Module 13-append_after
inserts a line after each specific
line in a text file
"""


def append_after(filename="", search_string="", new_string=""):
    """
    function to insert line
    """
    with open(filename, mode="r", encoding="utf-8") as file:
        lines = file.readlines()
    with open(filename, mode="w", encoding="utf-8") as file:
        for lin in lines:
            file.write(lin)
            if search_string in lin:
                file.write(new_string)
