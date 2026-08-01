#!/usr/bin/python3
"""Module that provides a function to add two numbers together.

The function accepts integers or floats, truncates any float
argument down to an integer (no rounding), and returns the sum of
the two resulting integers.
"""


def add_integer(a, b=98):
    """Add two integers, or two numbers castable to integers.

    Args:
        a (int|float): The first value. Required.
        b (int|float): The second value. Defaults to 98.

    Returns:
        int: The sum of ``a`` and ``b`` after truncating any float
        argument to an integer.

    Raises:
        TypeError: If ``a`` is not an int or float.
        TypeError: If ``b`` is not an int or float.
    """
    if not isinstance(a, (int, float)) or isinstance(a, bool):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)) or isinstance(b, bool):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
