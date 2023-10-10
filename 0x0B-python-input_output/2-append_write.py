#!/usr/bin/python3
"""
Module 2-append_write
appends a string at the end of a text file
"""


def append_write(filename="", text=""):
    """
    appends a string at end and returns num of chars
    """
    with open(filename, mode="a", encoding="utf-8") as txtfile:
        added_chars = txtfile.write(text)
        return added_chars
