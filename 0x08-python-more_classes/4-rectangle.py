#!/usr/bin/python3
"""This is a module that defines a rectangle"""

class Rectangle:
    """ A class that defines a Rectangle class with diffrent method to set the height and width
    """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    def area(self):
        """Returns the area of the Rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """Return the perimeter of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height + self.__width) * 2

    def __str__(self):
        """prints out # for the number of width in ref to height
        and return the and empty string when width and height equal 0
        """
        if self.__height == 0 or self.__width == 0:
            return ""
        return '\n'.join('#' * self.__width for i in range(self.__height))

    def __repr__(self) -> str:
        """Returns the Class Rectangle Function"""
        return f"Rectangle({self.__width}, {self.__height})"
    @property
    def width(self):
        """Returns the rectangle width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle"""

        if not isinstance(value, int):
            raise TypeError("Width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Returns the rectangle Height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
