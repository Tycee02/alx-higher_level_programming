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
        if value >= 0:
            self.__width = value
        else:
            raise ValueError("Width must be a non-negative value.")

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
        if value >= 0:
            self.__height = value
        else:
            raise ValueError("Height must be a non-negative value.")

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
        self.__y = value
