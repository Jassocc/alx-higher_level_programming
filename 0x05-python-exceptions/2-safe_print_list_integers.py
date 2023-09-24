#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    pri = 0
    try:
        for a in range(x):
            if isinstance(my_list[a], int):
                print("{:d}".format(my_list[a]), end="")
                pri += 1
    except (TypeError, ValueError):
        continue
     print()
    return pri
