#!/usr/bin/python3
""" a function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False.
    Args:
        obj: the class instance
        a_class: the class to check
"""


def inherits_from(obj, a_class):
    """Function that Returns True or False"""
    return isinstance(obj, a_class) and type(obj) is not a_class
