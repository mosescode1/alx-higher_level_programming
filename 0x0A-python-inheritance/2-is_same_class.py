#!/usr/bin/python3
"""a function that returns True if the object is exactly an instance of the specified class ; otherwise False.
    Args:
        obj: the class instance
        a_class: the class to check
"""


def is_same_class(obj, a_class):
    """Function that Returns True or False"""
    return isinstance(type(obj), a_class)


print(is_same_class(2, int))