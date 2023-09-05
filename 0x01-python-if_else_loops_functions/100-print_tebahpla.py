#!/usr/bin/python3
for char in range(0, 26):
    u = ord('z') - char
    if char % 2 == 1:
        u = (chr(u - ord('a') + ord('A')))
    else:
        u = chr(u)
    print("{}".format(u), end='')
