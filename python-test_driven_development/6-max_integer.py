#!/usr/bin/python3
"""Module that provides a function to find the max integer in a list."""


def max_integer(list=[]):
    """Find and return the max integer in a list of integers.

    Args:
        list (list): A list of integers or floats. Defaults to [].

    Returns:
        The largest element of ``list``, or ``None`` if ``list`` is
        empty.
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result
