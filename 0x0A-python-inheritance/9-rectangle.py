#!/usr/bin/python3
"""This Module is based on Based Geometry"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry

class Rectangle(BaseGeometry):
    """A rectangle class inherits from BaseGeometry"""
    def __init__(self, width, height):
        """Intilizing Rectangle with width and height"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """Returns a string reoresentatiom"""
        return f"[Rectangle] {self.__width}/{self.__height}"
    
    def area(self):
        """Returns the area of a rectangle"""
        return self.__width * self.__height
    
