#!/usr/bin/python3
"""Write to a file."""


def write_file(filename="", text=""):
    """writes a string to a utf8 file
    Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.
    Returns:
        The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
