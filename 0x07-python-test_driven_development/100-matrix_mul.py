#!/usr/bin/python3
"""
Module 100-matrix_mul
MAtrix multiplication definitions
size, lists and rows mus tbe the same
"""


def matrix_mul(m_a, m_b):
    """
    matrix multiplciation 
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    for row in m_a:
        if type(row) is not list:
            raise TypeError("m_a must be a list of lists")
    for row in m_b:
        if type(row) is not list:
            raise TypeError("m_b must be a list of lists")
    if len(m_a) == 0 or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    for er in m_a:
        for a in er:
            if not isinstance(a, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
        if len(er) != len(m_a[0]):
            raise TypeError("each row of m_a must be of the same size")
        if len(er) != len(m_b):
            raise ValueError ("m_a and m_b can't be multiplied")
    for er in m_b:
        for a in er:
            if not isinstance(a, (int, float)):
                raise TypeError("m_b should contain only integers or floats")
            if len(er) != len(m_b[0]):
                raise TypeError("each row of m_b must be of the same size")
    lin = []
    matr = []
    a = 0
    for row_one in range(len(m_a)):
        lin = []
        for colu_two in range(len(m_b[0])):
            for j in range(len(m_a[0])):
                a += m_a[row_one][j] * m_b[j][colu_two]
            lin.append(a)
            a = 0
        matr.append(lin)
    return matr
