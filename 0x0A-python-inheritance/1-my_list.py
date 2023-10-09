#!/usr/bin/python3
"""
Module 1-my_list

a class that inherits from class lists
"""


class MyList(list):
    """
    class that inherits all the properties
    from the class known as list
    """
    def __init__(self, *args):
        super().__init__(*args)

    def print_sorted(self):
        """
        function that prints the list in
        asc order
        """
        print(sorted(self))
