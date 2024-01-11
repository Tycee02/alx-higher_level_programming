#!/usr/bin/python3
"""1-write_file.py"""


def write_file(filename="", text=""):
    """writes a string to a text file(UTF8)
    Returns: number of characters written
    """
    with open(filename, 'w', encoding="utf-8") as f:
        count = f.write(text)

    return count
