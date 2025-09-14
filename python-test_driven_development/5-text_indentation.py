#!/usr/bin/python3
"""
This module provides a function to indent text with two new lines
after '.', '?' and ':'.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after '.', '?' and ':'.

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    i = 0
    while i < len(text):
        char = text[i]
        result += char
        if char in ".?:":
            result += "\n\n"
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1

    for line in result.split("\n"):
        print(line.strip())
