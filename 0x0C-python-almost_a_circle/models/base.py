#!/usr/bin/python3
import json
"""
    This is a modile a python package
"""


class Base:
    """
        Base class useed throughout the task
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + ".json"
        json_list = [obj.to_dictionary() for obj in list_objs]

        with open(filename, 'w') as file:
            file.write(cls.to_json_string(json_list))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            return "[]"
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            instances = cls(10, 30)
        elif cls.__name__ == "Square":
            instances = cls(9)

        instances.update(**dictionary)
        return instances

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + '.json'

        if not filename:
            return "[]"

        with open(filename, 'r') as file:
            json_data = file.read()
            obj_dicts = cls.from_json_string(json_data)
            return [cls.create(**obj) for obj in obj_dicts]


# b1 = Base()
# dicts = {'name': 'moses', 'age': 30}

# value = b1.to_json_string(dicts)
# print(type(value))
