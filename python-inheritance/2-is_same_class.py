#!/usr/bin/python3
"""Module that defines a function to check for exact class matches."""


def is_same_class(obj, a_class):
    """Check if obj is exactly an instance of a_class."""
    return type(obj) == a_class
