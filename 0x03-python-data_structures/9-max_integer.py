#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    max_n = my_list[0]
    for big in my_list:
        if big > max_n:
            max_n = big
    return max_n
