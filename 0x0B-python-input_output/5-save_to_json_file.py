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

filename = "my_dict.json"
my_dict = { 
    'id': 12,
    'name': "John",
    'places': [ "San Francisco", "Tokyo" ],
    'is_active': True,
    'info': {
        'age': 36,
        'average': 3.14
    }
}
save_to_json_file(my_dict, filename)