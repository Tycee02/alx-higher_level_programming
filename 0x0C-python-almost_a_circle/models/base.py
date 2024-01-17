#!/usr/bin/python3
"""base.py"""


class Base:
    """
    The Base class serves as a base class for other classes and includes
functionality for managing unique identifiers.

    Attributes:
    __nb_objects (int): A class variable to keep track
of the number of objects created.
    id (int): An instance variable representing the
unique identifier assigned to an object.

    Methods:
    __init__(self, id=None):
        Initializes a Base object with a unique identifier.
        If 'id' is provided, the object is assigned that identifier;
otherwise, a new identifier is generated.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a Base object with a unique identifier.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries.
        """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
