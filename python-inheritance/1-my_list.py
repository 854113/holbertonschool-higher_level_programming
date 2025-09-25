#!/usr/bin/python3
"""Defines the MyList class that inherits from list."""


class MyList(list):
    """Custom list class that inherits from Python's built-in list."""

    def print_sorted(self):
        """Print the list in ascending sorted order.

        Assumes all elements are integers.
        Does not modify the original list.
        """
        print(sorted(self))
