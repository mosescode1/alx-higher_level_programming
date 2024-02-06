#!/usr/bin/python3
"""A module that hat returns the JSON representation of 
    an object (string):
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
