#!/usr/bin/python3
"""2-append_write.py"""


def append_write(filename="", text=""):
    """append a string at the end of a text file(UTF8)
    Returns: number of characters added
    """
    with open(filename, 'a', encoding="utf-8") as f:
        count = f.write(text)

    return count
