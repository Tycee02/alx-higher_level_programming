#!/usr/bin/python3
"""6-load_from_json_file.py"""
import json


def load_from_json_file(filename):
    """Function that creates an object from a JSON file"""
    with open(filename, "r", encoding="utf-8") as f:
        obj = json.load(f)

    return obj
