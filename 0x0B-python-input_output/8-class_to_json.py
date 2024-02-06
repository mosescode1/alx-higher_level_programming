#!/usr/bin/python3
"""
    A Module that returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean) for JSON serialization of an object:
"""

def class_to_json(obj):
    """A funtion that serilize a class object to a json object"""
    dict_obj = obj.__dict__
    for key, value in dict_obj.items():
        if isinstance(value, (int, str, dict, bool, list)):
            dict_obj[key] = value
        elif isinstance(value, (tuple, set)):
            dict_obj[key] = list(value)
        elif hasattr(value, '__dict__'):
            dict_obj[key] = class_to_json(value)

    return dict_obj
