#!/usr/bin/python3
""" A Module Student"""


class Student:
    """A class for student"""
    def __init__(self, first_name, last_name, age):
        """intilize new variables"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionsry Representation"""
        new_dict = dict()
        dict_obj = self.__dict__
        if attrs:
                for key, value in dict_obj.items():
                    if key in attrs:
                        if isinstance(value, (int, bool, str, dict, list)):
                            new_dict[key] = value
                        elif isinstance(value, (tuple, list)):
                            new_dict[key] = list(value)
                        elif hasattr(value, '__dict__'):
                            new_dict = self.to_json(value)
                return new_dict
            
        return dict_obj
