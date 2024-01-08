#!/usr/bin/python3
"""4-inherits_from.py"""


def inherits_from(obj, a_class):
    """Fuction that check if an object is an instance of a class that
    inherited(directly or indirectly) from the specified class
    Return: True or False
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
