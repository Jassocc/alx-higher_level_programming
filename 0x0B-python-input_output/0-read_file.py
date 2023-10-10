#!/usr/bin/python3
"""
Module -0 contains a file
that reads from a text file
"""


def read_file(filename=""):
    """
    Function that reads from a file
    """
    with open(filename, mode="r", encoding="utf-8") as file:
        res = file.read()
        print(res, end="")
