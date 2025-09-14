#!/usr/bin/python3
"""
This module provides a function to divide all elements
of a matrix by a given divisor.
All divisions are rounded to 2 decimal places.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a number.

    Args:
        matrix: list of lists containing integers/floats
        div: number (int or float) to divide by

    Returns:
        A new matrix with elements divided by div,
        rounded to 2 decimal places.

    Raises:
        TypeError: if matrix is not a proper matrix
                   or if div is not a number
        ZeroDivisionError: if div == 0
    """
    
    if (not isinstance(matrix, list) or
            not all(isinstance(row, list) for row in matrix) or
            not all(isinstance(elem, (int, float))
                    for row in matrix for elem in row)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(elem / div, 2) for elem in row] for row in matrix]
