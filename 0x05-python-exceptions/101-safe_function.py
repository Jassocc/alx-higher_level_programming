#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        res = fct(*args)
        return res
    except (ZeroDivisionError, IndexError, TypeError, ValueError) as e:
        sys.stderr.write("Exception: {}\n".format(e))
        return None
