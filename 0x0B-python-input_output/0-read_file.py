#!/usr/bin/python3
"""Read file and print line"""


def read_file(filename=""):
    """reads a text file (UTF8) and prints to stdout"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
