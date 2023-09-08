#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for r in matrix:
        for el in r:
            if el is not r[len(r) - 1]:
                print("{:d}".format(el), end=" ")
            else:
                print("{:d}".format(el), end="")
        print()
