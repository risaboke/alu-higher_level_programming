#!/usr/bin/python3
"""Module that provides a function to pretty-print a block of text,
inserting two new lines after every ``.``, ``?`` and ``:`` while
stripping any leading or trailing spaces from each printed line.
"""


def text_indentation(text):
    """Print ``text`` with two new lines after each ``.``, ``?`` or ``:``.

    Args:
        text (str): The text to print.

    Raises:
        TypeError: If ``text`` is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    stop_chars = ".?:"
    at_line_start = True
    for char in text:
        if char == " " and at_line_start:
            continue
        print(char, end="")
        at_line_start = False
        if char in stop_chars:
            print("\n")
            at_line_start = True
