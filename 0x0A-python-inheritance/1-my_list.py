#!/usr/bin/python3
"""A class list"""



class MyList(list):
    """A list that inherits from list"""
    def print_sorted(self):
        """Returns a Sorted list"""
        print(sorted(self))
