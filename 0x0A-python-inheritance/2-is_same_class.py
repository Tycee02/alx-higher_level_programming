#!/usr/bin/python3
"""Function that returns True or False"""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of the specified class
    Return: True or false
    """
    return type(obj) == a_class
