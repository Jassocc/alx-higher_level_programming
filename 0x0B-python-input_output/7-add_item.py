#!/usr/bin/python3
"""
Module 7-add_item
Adds all args to a python list using
previous implementations
"""
import sys
from os.path import exists


save = __import__("5-save_to_json_file").save_to_json_file
load = __import__("6-load_from_json_file").load_from_json_file


filename = "add_item.json"
if exists(filename):
    my_list = load(filename)
else:
    my_list = []
my_list.extend(sys.argv[1:])
save(my_list, filename)
