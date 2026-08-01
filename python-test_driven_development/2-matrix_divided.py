#!/usr/bin/python3
"""Module that provides a function to divide every element of a
matrix (a list of lists of integers or floats) by a given number,
returning a brand new matrix without mutating the original one.
"""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix by ``div``.

    Args:
        matrix (list): A list of lists of integers or floats.
            Every row must have the same length.
        div (int|float): The number to divide each element by.
            Cannot be equal to 0.

    Returns:
        list: A new matrix with every element divided by ``div``
        and rounded to 2 decimal places.

    Raises:
        TypeError: If ``matrix`` is not a list of lists of
            integers/floats.
        TypeError: If the rows of ``matrix`` don't all have the
            same size.
        TypeError: If ``div`` is not an integer or a float.
        ZeroDivisionError: If ``div`` is equal to 0.
    """
    matrix_error = (
        "matrix must be a matrix (list of lists) of integers/floats")

    if not isinstance(matrix, list) or matrix == []:
        raise TypeError(matrix_error)

    for row in matrix:
        if not isinstance(row, list) or row == []:
            raise TypeError(matrix_error)
        for element in row:
            if not isinstance(element, (int, float)) or isinstance(
                    element, bool):
                raise TypeError(matrix_error)

    if len(set(len(row) for row in matrix)) != 1:
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)) or isinstance(div, bool):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(element / div, 2) for element in row] for row in matrix]
