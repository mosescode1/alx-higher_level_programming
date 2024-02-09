#!/usr/bin/python3
"""A class that inherits from the Rectangle class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(id=id, width=size, height=size, x=x, y=y)
        self.size = size

    def __str__(self):
        return "[{}] ({}) {}/{} - {}".format(
            'Square',
            self.id,
            self.x,
            self.y,
            self.size
            )

    @property
    def size(self):
        return self.__width

    @size.setter
    def size(self, width_value):
        if not isinstance(width_value, int):
            raise TypeError("width must be an integer")
        elif width_value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width_value

    def update(self, *args, **kwargs):
        if args:
            if len(args) == 1:
                self.id = args[0]
            elif len(args) == 2:
                self.id, self.size = args
            elif len(args) == 3:
                self.id, self.size, self.x = args
            elif len(args) == 4:
                self.id, self.size, self.x, self.y = args
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.size = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

    def to_dictionary(self):
        diction = dict()
        diction['id'] = self.id
        diction['x'] = self.x
        diction['size'] = self.size
        diction['y'] = self.y
        return diction
