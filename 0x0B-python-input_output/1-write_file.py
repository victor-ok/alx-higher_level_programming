#!/usr/bin/python3
"""defines a function that writes a string to a txt file"""


def write_file(filename="", text=""):
    """
    write a string to a UTF8 txt file.

    Args:
        filenmae(str): the name of the file to write to
        text(str): the txt to write to a file
    Returns:
        the number of characters written
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
