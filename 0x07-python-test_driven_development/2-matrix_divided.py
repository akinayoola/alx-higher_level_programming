#!/usr/bin/python3
"""Defines a matrix division function."""

def matrix_divided(matrix, div):

    """Divides element of a given matrix.

    Args:
        matrix (list): a matrix of rows and column
        div (a float or integer)

    Raises:
        TypeError: matrix must be a matrix (list of lists) of integers/floats
        TypeError: Each row of the matrix must have the same size
        TypeError: div must be a number
        ZeroDivisionError: division by zero

    Returns a new matrix
    """

    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or 
            not all((isinstance(ele, int) or isinstance(ele, float))
                for ele in [num for row in matrix for num in row])):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])

    return (new_matrix)





