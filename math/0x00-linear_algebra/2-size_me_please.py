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
    for matrice in matrix:
        nbmatrice = len(matrix)
        for line in matrice:
            if type(line) == list:
                nbline = len(matrice)
                nbcolumn = len(line)
                size = [nbmatrice, nbline, nbcolumn]
            else:
                for line in matrix:
                    nbline = len(matrix)
                    nbcolumn = len(line)
                    size = [nbline, nbcolumn]
    return size
