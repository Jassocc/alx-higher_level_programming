#!/usr/bin/python3
"""
Module 101-lazy-matrix-mul
matrix matrix mult with numpy
Use numpy module
"""
import numpy

def lazy_matrix_mul(m_a, m_b):
    """
    multiply m_a and _mb
    """
    num = numpy.matmul(m_a, m_b)
    return num
