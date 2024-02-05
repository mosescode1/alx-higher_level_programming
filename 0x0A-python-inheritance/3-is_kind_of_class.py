#!/usr/bin/python3
"""a function that returns True if the object is exactly an instance of the specified class ; otherwise False.
    Args:
        obj: the class instance
        a_class: the class to check
"""


def is_kind_of_class(obj, a_class):
    """Function that Returns True or False"""
    return isinstance(obj, a_class)
