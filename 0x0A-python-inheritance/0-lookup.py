#!/usr/bin/python3
"""0-lookup.py"""


def lookup(obj):
    """List the available attributes and methods of an object
    Args:
        obj: object whose attribute and method to be listed
    Returns: a list of object
    """
    return list(dir(obj))
