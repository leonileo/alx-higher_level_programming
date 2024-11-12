#!/usr/bin/python3

"""This module has a function that divides all the elemnts in a matrix."""


def matrix_divided(matrix, div):
    """This function divides all elements of the matrix by the provided div.

    Example:
    matrix_divided([[1, 2], [3, 4]], 2)
    Returns:
    [[0.5, 1.0], [1.5, 2.0]]
    """

    # validating the matrix and the div
    if not isinstance(matrix, list):
        raise TypeError(
            'matrix must be a matrix (list of lists) of integers/floats'
        )
    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')

    new_matrix = []

    # divide the elements by looping throgh the matrix
    for i in range(len(matrix)):
        # checking if the element in the matrix is a list
        if not isinstance(matrix[i], list):
            raise TypeError(
                'matrix must be a matrix (list of lists) of integers/floats'
            )
        # checking the length of each list in the matrix
        if len(matrix[i]) != len(matrix[0]):
            raise TypeError('Each row of the matrix must have the same size')

        new_row = []

        # loop through the elements in the list
        for j in matrix[i]:
            if not isinstance(j, (int, float)):
                raise TypeError(
                    'matrix must be a matrix (list of lists)'
                    'of integers/floats')
            new_row.append(round((j / div), 2))
        new_matrix.append(new_row)

    return new_matrix
