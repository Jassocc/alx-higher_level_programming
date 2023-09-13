#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_direc = {}
    temp = {}
    for k, v in a_dictionary.items():
        n = v * 2
        temp = {k: temp}
        new_direc.update(temp)
    return new_direc
