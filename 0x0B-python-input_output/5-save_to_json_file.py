#!/usr/bin/python3

"""
    A Module that writes an Object to a text file, using a JSON representation:
"""

import json


def save_to_json_file(my_obj, filename):
    """A function That deserilize a python object and saves it to a file"""
    with open(filename, 'w', encoding="UTF8") as f:
        data = json.dumps(my_obj)
        f.write(data)
