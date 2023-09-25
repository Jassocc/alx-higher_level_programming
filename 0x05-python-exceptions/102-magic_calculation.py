#!/usr/bin/python3
def magic_calculation(a, b):
    res = 0
    for arr in range(1, 3):
        try:
            if arr > a:
                raise Exception("Too far")
            res += (a ** b) / arr
        except:
            res = b + a
            break
    return res
