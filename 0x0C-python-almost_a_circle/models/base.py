#!/usr/bin/python3
"""base.py"""
import json


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

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes JSON representation to a file.
        """
        file_name = cls.__name__ + ".json"
        new_list = []
        if list_objs is not None:
            for i in list_objs:
                new_list.append(cls.to_dictionary(i))
        with open(file_name, 'w') as json_file:
            json_file.write(cls.to_json_string(new_list))

    @staticmethod
    def from_json_string(json_string):
        """
        Returns a list of JSON string representation.
        """
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    def update(self, *args, **kwargs):
        """
        Update the instance attributes with the provided values.

        Parameters:
        - *args: Positional arguments.
        - **kwargs: Keyword arguments.
        """
        if args:
            for key, value in zip(self.__dict__.keys(), args):
                setattr(self, key, value)
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    @classmethod
    def create(cls, **dictionary):
        """
        Create an instance of the class with attributes set from the provided dictionary.

        Parameters:
        - **dictionary: Double pointer to a dictionary containing attribute names and values.

        Returns:
        - Instance of the class with attributes set.
        """
        instance = cls.__new__(cls)
        instance.update(**dictionary)
        return instance
