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
        
    def area(self):
        """Method to calculate the area of a square"""
        value = self.__size ** 2
        return value
    @property
    def size(self):
        """return the size of the square"""
        return self.__size
    
    @size.setter
    def size(self, value):
        """Set the size of the square """
        self.__size = value
        
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")

    def my_print(self):
        """a loop thats prints out a {"#"} according to value of size"""
        for _ in range((self.__size)):
            for i in range(self.__size):
                print("#", end="")
            print()
