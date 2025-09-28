#!/usr/bin/python3
"""Script that defines a class called BaseGeometry"""


class BaseGeometry:
    """Represents a class called base geometry"""
    def area(Self):
        raise Exception("area() is not implemented")


def integer_validator(self, name, value):
    if type(value) is not int:
        raise TypeError("{} must be an integer".format(name))
    if value <= 0:
        raise ValueError("{} must be greater than 0".format(name))
