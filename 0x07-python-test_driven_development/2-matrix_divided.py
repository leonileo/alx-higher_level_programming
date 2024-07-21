#!/usr/bin/python3

"""
This module has a function matrix_divided() that returns a new matrix from the provided list of matrix.
"""


def matrix_divided(matrix, div):
    if (type(matrix) is not list):
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    for i in matrix:
        if(type(i) is not list):
            raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
        for j in i:
            if((type(j) is not int) and (type(j) is not float)):
                raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
        if len(i) != len(matrix[0]):
            raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    return [[round(x / div, 2) for x in i] for i in matrix]
