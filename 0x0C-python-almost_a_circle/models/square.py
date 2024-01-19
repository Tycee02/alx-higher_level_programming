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
        Returns the Square custom representation.
        """
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x,
                                                 self.y,
                                                 self.size)

    def __init__(self, size):
        super().__init__(size, size)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
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
