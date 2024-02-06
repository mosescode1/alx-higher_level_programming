#!/usr/bin/python3

"""
    A Module that returns an object 
    (Python data structure) 
    represented by a JSON string:
"""


import json


def from_json_string(my_str):
    """
    A function that returns deserilize a python object
    """
    
    data = json.loads(my_str)
    return data
