#!/usr/bin/python3
"""Module that defines a Square class with a private size attribute."""


class Square:
    """Represent a square defined by its size."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size: The size of the square.
        """
        self.__size = size
