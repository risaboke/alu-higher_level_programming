#!/usr/bin/python3
"""Module that defines a function to check strict class inheritance."""


def inherits_from(obj, a_class):
    """Check if obj is an instance of a class that inherits from a_class."""
    return isinstance(obj, a_class) and type(obj) != a_class
