#!/usr/bin/env python3
"""script that calculates the shape of a matrix"""


def matrix_shape(matrix):
    """function that calculates the shape of a matrix
        Args:
            matrix: matrix to size
        Return:
            size of the matrix
    """
    size = []
    while type(matrix) == list:
        size.append(len(matrix))
        matrix = matrix[0]
    return size
