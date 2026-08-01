#!/usr/bin/python3
"""Module that provides a function to print someone's full name in
the format ``My name is <first name> <last name>``.
"""


def say_my_name(first_name, last_name=""):
    """Print ``My name is <first_name> <last_name>``.

    Args:
        first_name (str): The first name. Required.
        last_name (str): The last name. Defaults to an empty string.

    Raises:
        TypeError: If ``first_name`` is not a string.
        TypeError: If ``last_name`` is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
