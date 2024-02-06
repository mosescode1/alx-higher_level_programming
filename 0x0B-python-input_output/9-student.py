#!/usr/bin/python3
""" A Module Student"""


class Student:
    """A class for student"""
    def __init__(self, first_name, last_name, age):
        """intilize new variables"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return a dictionsry Representation"""
        dict_obj = self.__dict__
        for key, value in dict_obj.items():
            if isinstance(value, (int, bool, str, dict, list)):
                dict_obj[key] = value
            elif isinstance(value, (tuple, list)):
                dict_obj[key] = list(value)
            elif hasattr(value, '__dict__'):
                dict_obj = self.to_json(value)
            
        return dict_obj
