#!/usr/bin/python3
"""a function that returns True if the object is exactly an instance of the specified class ; otherwise False.
    Args:
        obj: the class instance
        a_class: the class to check
"""


def is_same_class(obj, a_class):
    """Check if they are same object"""
    return type(obj) is a_class
