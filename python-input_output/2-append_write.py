#!/usr/bin/python3
"""Module that appends a string to the end of a text file."""


def append_write(filename="", text=""):
    """Append a string to a UTF8 text file and return the number added."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
