#!/usr/bin/python3
"""Module that defines a class extending the built-in list type."""


class MyList(list):
    """A list that can also print its contents in sorted order."""

    def print_sorted(self):
        """Print the list in ascending sorted order."""
        print(sorted(self))
