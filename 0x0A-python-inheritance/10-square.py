#!/usr/bin/python3
"""This Module is based on Based Geometry"""
Rectangle = __import__("9-rectangle").Rectangle

class Square(Rectangle):
    """Square class inherits from a subclass Rectangle"""
    def __init__(self, size):
        """intilizing Square and intilizing the methods of Rectangle"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
