#!/usr/bin/python3
"""
Module 14-stats
reads line by line and computes the metrics
"""
import sys


def print_stats(size, status_codes):
    """
    prints statistics
    """
    print("File size: {}".format(size))
    for status_code, val in sorted(status_codes.items()):
        if val:
            print("{:s}: {:d}".format(status_code, val))


def parse_line():
    """
    pareses lines
    """
    size = 0
    li = 0
    status_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                    "403": 0, "404": 0, "405": 0, "500": 0}
    try:
        for line in sys.stdin:
            fi = list(map(str, line.strip().split(" ")))
            size += int(fi[-1])
            if fi[-2] in status_codes:
                status_codes[fi[-2]] += 1
            li += 1
            if li % 10 == 0:
                print_stats(size, status_codes)
    except KeyboardInterrupt:
        print_stats(size, status_codes)
        raise
    print_stats(size, status_codes)


parse_line()
