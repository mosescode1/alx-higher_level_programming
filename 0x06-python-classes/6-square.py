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
    def __init__(self, size=0, position=(0, 0)) -> None:
        """initilizing a new attribute called size"""
        self.__size = size
        self.__position = position

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

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

    @property
    def position(self):
        self.__position

    @position.setter
    def position(self, value):
        """set the position value"""
        self.__position = value
        if len(self.__position) != 2 and not isinstance(self.__position, tuple)or not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")


    def area(self):
        """Method to calculate the area of a square"""
        value = self.__size ** 2
        return value
    
    def my_print(self):
        """a loop thats prints out a {"#"} according to value of size"""
        if self.size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
        
        for _ in range((self.__size)):
            print(" " * self.__position[0], end="")
            for i in range(self.__size):
                print("#", end="")
            print()
