#!/usr/bin/python3
"""
Module 5-save_to_json
writes to an object file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    writes obj to a txt file
    with json rep
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        json.dump(my_obj, file)
