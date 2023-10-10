#!/usr/bin/python3
"""
Module 14-stats
reads line by line and computes the metrics
"""
import sys


def print_stats(total_size, status_codes):
    """
    prints statistics
    """
    try:
        print("File size: {}".format(total_size))
        for status_code in sorted(status_codes.keys()):
            print("{}: {}".format(status_code, status_codes[status_code]))
    except BrokenPipeError:
        pass

    def parse_line(line):
        """
        pareses lines
        """
        parts = line.split()
        if len(parts) < 9:
            return None
        status_code = parts[-2]
        file_size = parts[-1]
        return status_code, int(file_size)

    def update_stats(status_code, file_Size, total_size, status_codes):
        """
        updates stats
        """
        total_size += file_size
        if status_code in status_codes:
            status_codes[status_code] += 1
        return total_size
    total_size = 0
    status_codes = {}
    try:
        for a, line in enumerate(sys.stdin, start=1):
            line = line.strip()
            pars = parse_line(line)
            if pars is not None:
                status_code, file_size = pars
                total_size = update_stats(status_code,
                                          file_size, total_Size, status_codes)
            if a % 10 == 0:
                print_stats(total_size, status_codes)
    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
