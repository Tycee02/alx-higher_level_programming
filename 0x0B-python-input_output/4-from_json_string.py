#!/usr/bin/python3
"""4-from_json_string.py"""
import json


def from_json_string(my_str):
    """Returns an object(Python data structure) represented ba a JSON string"""
    return json.loads(my_str)
