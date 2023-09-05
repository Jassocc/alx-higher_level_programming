#!/usr/bin/python3
def uppercase(str):
    res = ""
    for char in str:
        if 'a' <= char <= 'z':
            upper = chr(ord(char) - ord('a') + ord('A'))
            res += upper
        else:
            res += char
        print(res)
