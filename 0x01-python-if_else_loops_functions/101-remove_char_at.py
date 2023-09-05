#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0 or n >= len(str):
        return (str)
    res = ""
    for a in range(len(str)):
        if a != n:
            res = res + str[a]
    return (res)
