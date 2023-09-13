#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_direc = {}
    for k, v in a_dictionary.items():
        new_direc[k] = v * 2
    return new_direc
