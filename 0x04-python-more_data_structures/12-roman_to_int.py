#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    rom_val = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            }
    res = 0
    prev = 0
    for a in range(len(roman_string)-1, -1, -1):
        curr_v = rom_val[roman_string[a]]
        if curr_v >= prev:
            res = res + curr_v
        else:
            res = res - curr_v
        prev = curr_v
    return res
