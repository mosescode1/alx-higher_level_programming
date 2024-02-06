#!/usr/bin/python3
"""A module that that appends to a text file (UTF8) and 
    returns number of characters added
"""
import json


def to_json_string(my_obj):
    """Function that converst a python representation of 
    an object to string
    Args:
        my_obj(python object) : to be serlizied
    """
    data = json.dumps(my_obj)
    return data
