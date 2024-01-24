#!/usr/bin/python3
"""This is a documentation for a square module
    there is no functionality to it
 """
class Square:
    """
    Description of the class Square

    Attributes:
        size: The size of a square is crucial for a square, many things depend of it
    """
    def __init__(self, size=0) -> None:
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
