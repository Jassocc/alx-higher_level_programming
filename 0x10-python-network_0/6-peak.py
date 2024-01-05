#!/usr/bin/python3
"""
Write a function that finds a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """
    def to find the peak
    """
    if not list_of_integers:
        return None
    low, high = 0, len(list_of_integers) - 1
    while low < high:
        mid = (low + high) // 2
        if list_of_integers[mid] > list_of_integers[mid + 1]:
            high = mid
        elif list_of_integers[mid] == list_of_integers[mid + 1]:
            low = mid + 1
        else:
            low = mid + 1
    if low + 1 < len(list_of_integers):
        return max(list_of_integers[low], list_of_integers[low + 1])
    else:
        return list_of_integers[low]
