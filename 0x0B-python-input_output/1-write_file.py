#!/usr/bin/python3
"""
Contains a module that wrtes a 
string to a text file
"""


def write_file(filename="", text=""):
    """
    function that returns the num of chars
    """
    with open(filename, mode="w", encoding="utf-8") as txtfile:
        num_char = txtfile.write(text)
        return num_char
