#!/usr/bin/python3
"""
Module 12-pascal-triangle
returns list of integeres representing
pascals triangle
"""


def pascal_triangle(n):
    """
    function for thge triangle
    """
    if n <= 0:
        res = []
        return res
    trio = [[1]]
    for a in range(1, n):
        r = [1]
        for b in range(1, a):
            r.append(trio[a-1][b-1] + trio[a-1][b])
        r.append(1)
        trio.append(r)
    return trio
