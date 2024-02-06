#!/usr/bin/python3

"""
    A Module that creates an Object from a “JSON file”:
"""

import json


def load_from_json_file(filename):
    """Funtion that deserilize the content of a file"""
    with open(filename, 'r', encoding="UTF8") as f:
        data = f.read()
        return json.loads(data)
