#!/usr/bin/python3
"""
Module 2
Function that divides all elements of a matrix
using the prototype:
    def matrix_divided(matrix, div):
"""


def matrix_divided(matrix, div):
    """
    this divides all elements of a matrix and returns a new one
    """
    if not isinstance(matrix, list) or len(matrix) == 0 or len(matrix[0]) == 0:
        raise TypeError("matrix must be a matrix "
                        "(list of lists) of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    row_length = len(matrix[0])
    for row in matrix:
        if type(row) is not list or len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
        for elements in row:
            if not isinstance(elements, (int, float)):
                raise TypeError("matrix must be a matrix "
                                "(list of lists) of integers/floats")
    new_mat = []
    for row in matrix:
        new_row = []
        for elements in row:
            new_row.append(round(elements / div, 2))
        new_mat.append(new_row)
    return new_mat
