#!/usr/bin/env python3
"""script that adds two matrices"""


def add_matrices(mat1, mat2):
    """function that adds two matrices
        Args:
            matrices to add
        Return:
            the addition, None if matrices are of different shape
    """
    if matrix_shape(mat1) != matrix_shape(mat2):
        return None

    # add arrays
    if type(mat1[0]) == int:
        return add_arrays(mat1, mat2)

    # add 2D matrices
    if type(mat1[0][0]) == int:
        return add_matrices2D(mat1, mat2)

    # get the lower matrice
    sum = []
    if type(mat1[0][0]) == list and len(mat1) == len(mat2) and \
       len(mat1[0]) == len(mat2[0]):
        for i in range(len(mat1)):
            sum.append(add_matrices(mat1[i], mat2[i]))
        return sum


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


def add_arrays(arr1, arr2):
    """function that adds two arrays
        Args:
            arrays to add
        Return:
            the addition, None if arrays are of different shape
    """
    if len(arr1) == len(arr2):
        result = [arr1[i] + arr2[i] for i in range(len(arr1))]
        return result
    else:
        return None


def add_matrices2D(mat1, mat2):
    """function that adds two 2D matrices
        Args:
            matrices to add
        Return:
            the addition, None if matrices are of different shape
    """
    if len(mat1) == 0 or len(mat2) == 0:
        return None
    if len(mat1) == len(mat2) and len(mat1[0]) == len(mat2[0]):
        result = [[mat1[i][j] + mat2[i][j] for j in range(len(mat1[0]))]
                  for i in range(len(mat1))]
        return result
    else:
        return None
