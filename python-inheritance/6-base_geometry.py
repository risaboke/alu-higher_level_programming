#!/usr/bin/python3
"""Module that defines a base geometry class with an area method."""


class BaseGeometry:
    """A base class for geometry shapes."""

    def area(self):
        """Raise an exception because area() is not implemented."""
        raise Exception("area() is not implemented")
