#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sor_key = sorted(a_dictionary.items())
    for a, b in sor_key:
        print("{}: {}".format(a, b))
