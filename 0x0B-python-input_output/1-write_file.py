#!/usr/bin/python3
"""write string and return no of characters"""


def write_file(filename="", text=""):
    """writes a string to a ut8 file

    Args:
        filename (str): The file name to write
        text (str): the text to be written
    Returns:
        The number of characters written
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)

