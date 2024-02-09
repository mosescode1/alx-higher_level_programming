"""A class that inherits from the base class"""
Base = __import__("base").Base


class Rectangle(Base):

    def __init__(self, width, height, x=0, y=0, id=None):

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")

        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")

        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @ property
    def width(self):
        """ Returns the width

        Returns:
            (private attribute): the private width
        """
        return self.__width

    @width.setter
    def width(self, width):
        """Set the width of the rectangle

        Args:
            width (int):
        Raises:
            ValueError: width must be > 0
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

    @ property
    def height(self):
        """ Returns the height

        Returns:
            int : height
        """
        return self.__height

    @height.setter
    def height(self, height):
        """ Height Setter

        Args:
            height (int): the value of height you want to assign/change

        Raises:
            ValueError: height must be > 0
        """

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

    @property
    def x(self):
        """Returns the Value of x

        Returns:
            (private attribute): the private variable x
        """
        return self.__x

    @x.setter
    def x(self, x_value):
        """Sets the value of x

        Args:
            x_value (int): values to assign to x

        Raises:
            ValueError: x must be >= 0
        """

        if not isinstance(x_value, int):
            raise TypeError("x must be an integer")
        elif x_value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x_value

    @property
    def y(self):
        """used to get the value ox y

        Returns:
            (private attribute): returns the value of y
        """
        return self.__y

    @y.setter
    def y(self, y_value):
        if not isinstance(y_value, int):
            raise TypeError("y must be an integer")
        elif y_value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y_value

    def area(self):
        return self.__width * self.__height

    def display(self):
        for _ in range(self.__height):
            for _ in range(self.__width):
                print("#", end="")
            print()
