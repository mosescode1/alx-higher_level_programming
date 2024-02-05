#!/usr/bin/python3
"""Function to return a list of attribues
    Args:
        obj: class attributes being passed
"""
def lookup(obj):
    """A function that returns the list of available attributes and methods of an object"""
    return dir(obj)

