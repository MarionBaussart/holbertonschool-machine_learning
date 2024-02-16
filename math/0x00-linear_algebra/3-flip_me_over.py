#!/usr/bin/env python3
"""script that returns the transpose of a 2D matrix"""


def matrix_transpose(matrix):
    """function that returns the transpose of a 2D matrix
        Args:
            matrix: matrix to transpose
        Return:
            transpose
    """
    transpose = [[matrix[i][j] for i in range(len(matrix))]
                 for j in range(len(matrix[0]))]
    return transpose
