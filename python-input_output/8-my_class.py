#!/usr/bin/python3
"""My class module."""


class MyClass:
    """A simple class used to demonstrate class_to_json."""

    def __init__(self, name):
        """Initialize a new MyClass instance."""
        self.name = name
        self.number = 0

    def __str__(self):
        """Return the string representation of a MyClass instance."""
        return "[MyClass] {} - {:d}".format(self.name, self.number)
