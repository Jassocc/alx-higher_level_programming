#!/usr/bin/python3
def no_c(my_string):
    res = ""
    for charac in my_string:
        if charac not in "cC":
            res += charac
    return res
