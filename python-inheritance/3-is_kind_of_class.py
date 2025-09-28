#!/usr/bin/python3
"""This module contains a function"""


def is_kind_of_class(obj, a_class):
    """bool function that returns True if the object is an instance, or if the
    object is an instance of a class that inherited from, the specified class,
    otherwise False"""

    return type(obj) is a_class or issubclass(obj.__class__, a_class)
