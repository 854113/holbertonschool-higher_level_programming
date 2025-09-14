#!/usr/bin/python3
"""
This module provides a function to print a square with '#'.
"""


def print_square(size):
    """
    Prints a square with the character '#'.

    Args:
        size: length of the square (int)

    Raises:
        TypeError: if size is not an integer
        ValueError: if size is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
