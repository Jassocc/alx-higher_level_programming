#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    tot = 0
    freq = 0
    for score, weight in my_list:
        tot = tot + score * weight
        freq = freq + weight
    return tot / freq if freq != 0 else 0
