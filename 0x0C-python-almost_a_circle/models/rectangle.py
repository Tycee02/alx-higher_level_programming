#!/usr/bin/python3
"""rectangle.py"""
from models.base import Base


class Rectangle(Base):
    """
    The Rectangle class represents a rectangle and
    inherits from the Base class.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a Rectangle object with the specified
        width, height, and position.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Getter method for the width attribute.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for the width attribute.

        Parameters:
        value (int): The new value for the width.
        """
        try:
            assert isinstance(value, int)
        except Exception as e:
            raise TypeError("width must be an integer.")
        if value <= 0:
            raise ValueError("Width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter method for the height attribute.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for the height attribute.

        Parameters:
        value (int): The new value for the height.
        """
        try:
            assert isinstance(value, int)
        except Exception as e:
            raise TypeError("height must be an integer.")
        if value <= 0:
            raise ValueError("Height must be > 0.")
        self.__height = value

    @property
    def x(self):
        """
        Getter method for the x attribute.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter method for the x attribute.

        Parameters:
        value (int): The new value for the x-coordinate.
        """
        try:
            assert isinstance(value, int)
        except Exception as e:
            raise TypeError("x must be an integer.")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Getter method for the y attribute.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter method for the y attribute.

        Parameters:
        value (int): The new value for the y-coordinate.
        """
        try:
            assert isinstance(value, int)
        except Exception as e:
            raise TypeError("y must be an integer.")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Returns the area value of the Rectangle.
        """
        return self.__width * self.__height

    def display(self):
        """
        function that print visual representation of the rectangle by
printing empty lines, leading spaces, and # characters.
        """
        for line in range(self.__y):
            print()

        for i in range(self.__height):
            for space in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """
        str method to return rectangle representation
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id,
            self.__x,
            self.__y,
            self.__width,
            self.__height
        )

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""
        if args:
            for i, j in enumerate(args):
                if i == 0:
                    self.id = j
                elif i == 1:
                    self.width = j
                elif i == 2:
                    self.height = j
                elif i == 3:
                    self.x = j
                elif i == 4:
                    self.y = j

            for key, value in kwargs.items():
                setattr(self, key, value)
