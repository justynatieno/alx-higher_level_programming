#!/usr/bin/python3


"""prints a new line after the given characters."""


def text_indentation(text):
    """function to print new line after ., ? and :
    Args:
        text (str): the string to be altered
    Raises:
        TypeError: when text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1
