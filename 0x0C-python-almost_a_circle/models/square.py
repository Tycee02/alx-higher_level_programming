#!/usr/bin/python3
"""
square.py
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    The Square class represents a square and
    inherits from the Rectangle class.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square object with the specified size, position, and ID.
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """
        Returns a string representation of the Square.
        """
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x,
                                                 self.y,
                                                 self.size)

    @property
    def size(self):
        """
        retrieve size
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Set width and height with the same value
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value <= 0:
            raise ValueError("size must be > 0")

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Updates the Square attributes based on the arguments
or keyword arguments.
        """
        if len(args) == 0:
            for key, value in kwargs.items():
                self.__setattr__(key, value)
            return

        try:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]
        except IndexError:
            pass

    def to_dictionary(self):
        """
        Function that returns the dictionary representation
of a square
        """
        my_dict = {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
        return my_dict
