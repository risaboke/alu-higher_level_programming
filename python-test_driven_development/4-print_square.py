#!/usr/bin/python3
"""Module that provides a function to print a square of ``#``
characters of a given size, one row per line.
"""


def print_square(size):
    """Print a square with the ``#`` character.

    Args:
        size (int): The length of a side of the square. Must be
            an integer greater than or equal to 0.

    Raises:
        TypeError: If ``size`` is not an integer (this includes
            floats, whether positive or negative).
        ValueError: If ``size`` is an integer smaller than 0.
    """
    if not isinstance(size, int) or isinstance(size, bool):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
