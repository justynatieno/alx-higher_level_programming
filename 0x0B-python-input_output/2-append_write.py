#!/usr/bin/python3
"""Append to a string to a file"""


def append_write(filename="", text=""):
    """Appends a string to the end of a UTF8 text file.
    Args:
        filename (str): The name of the file to be appended to
        text (str): The string to be appended
    Returns:
        The number of characters appended.
    """

    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
