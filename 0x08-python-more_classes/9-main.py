#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
square2 = Rectangle(5, 9)
print("Area: {} - Perimeter: {}".format(square2.area(), square2.perimeter()))
print(square2)
my_square = Rectangle.square(5)
print("Area: {} - Perimeter: {}".format(my_square.area(), my_square.perimeter()))
print(my_square)
