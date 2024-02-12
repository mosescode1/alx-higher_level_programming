#!/usr/bin/python3
import json
from turtle import Turtle, Screen

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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        filename = cls.__name__ + '.csv'
        with open(filename, 'w') as f:
            f.write(list_objs)

    @staticmethod
    def draw(list_rectangles, list_squares):
        """draws all rectangles and squares"""
        turtle = Turtle()  # creating an instance of the Turtle class

        my_screen = Screen()  # instance of d screen class to pull up a window

        turtle.screen.bgcolor("coral")
        turtle.pensize(3)
        turtle.shape("turtle")
        turtle.color("#ffffff")

        for rect in list_rectangles:
            turtle.showturtle()
            turtle.up()
            turtle.goto(rect.x, rect.y)
            turtle.down()
            for i in range(2):
                turtle.forward(rect.width)
                turtle.left(90)
                turtle.forward(rect.height)
                turtle.left(90)
                turtle.hideturtle()

        turtle.color("#b5e3d8")
        for sq in list_squares:
            turtle.showturtle()
            turtle.up()
            turtle.goto(sq.x, sq.y)
            turtle.down()
            for i in range(2):
                turtle.forward(sq.width)
                turtle.left(90)
                turtle.forward(sq.height)
                turtle.left(90)
            turtle.hideturtle()

        my_screen.exitonclick()
