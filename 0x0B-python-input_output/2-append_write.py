#!/usr/bin/python3
"""defines a file appending function"""


def append_write(filename="", text=""):
    """
    Appends a string to the end of txt file

    Args:
        filename(str): the name of the file to append to.
        text(str): the string to be appended to the file.
    Returns:
        the number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
