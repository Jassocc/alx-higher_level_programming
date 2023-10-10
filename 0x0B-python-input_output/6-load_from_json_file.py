#!/usr/bin/python3
"""
Module 6-load_from_json
Loads object from another json file
"""
import json


def load_from_json_file(filename):
    """
    creates an object from json
    """
    with open(filename, mode="r", encoding="utf-8") as file:
        res = json.load(file)
        return res
