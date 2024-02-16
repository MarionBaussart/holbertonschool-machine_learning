#!/usr/bin/env python3
"""
module containing function minor
"""


def minor(matrix):
    """
    function that calculates the minor matrix of a matrix
    Args:
        matrix: list of lists whose minor matrix should be calculated
    Return: the minor matrix
    """
    minor = []

    if type(matrix) != list or len(matrix) == 0:
        raise TypeError("matrix must be a list of lists")
    for row in matrix:
        if type(row) != list:
            raise TypeError("matrix must be a list of lists")

        if len(matrix) != len(row) or \
                len(matrix) == 1 and len(row) == 0:
            raise ValueError("matrix must be a non-empty square matrix")

    # 1D matrix
    if len(matrix) == 1 and len(matrix[0]) == 1:
        return [[1]]

    # 2D matrix
    if len(matrix) == 2:
        minor.append(matrix[1][::-1])
        minor.append(matrix[0][::-1])

    # more than 3 dimensions matrix
    if len(matrix) > 2:
        for i in range(len(matrix)):
            det = []
            for j in range(len(matrix[0])):
                sub_matrix = get_sub_matrix(matrix, i, j)
                det.append(determinant(sub_matrix))
            minor.append(det)

    return minor


def get_sub_matrix(matrix, i, j):
    """
    function that give the sub matrix
    Args:
        matrix: list of lists
    Return: the sub matrix
    """
    sub_matrix = matrix[0:i] + matrix[i + 1:]

    return [row[0:j] + row[j + 1:] for row in sub_matrix]


def determinant(matrix):
    """
    function that calculates the determinant of a matrix
    Args:
        matrix: list of lists whose determinant should be calculated
    Return: the determinant of matrix
    """
    det = 0

    if type(matrix) != list or len(matrix) == 0:
        raise TypeError("matrix must be a list of lists")
    for row in matrix:
        if type(row) != list:
            raise TypeError("matrix must be a list of lists")

    # matrix = [[]]
    if len(matrix) == 1 and len(matrix[0]) == 0:
        return 1

    if len(matrix) != len(matrix[0]):
        raise ValueError("matrix must be a square matrix")

    # 1D matrix
    if len(matrix) == 1:
        return matrix[0][0]

    # 2D matrix
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    # more than 3 dimensions matrix
    rows = len(matrix)

    for i in range(rows):
        sub_matrix = matrix[1:]   # remove the ommited row
        for j in range(len(sub_matrix)):
            # remove the ommited column
            sub_matrix[j] = sub_matrix[j][:i] + sub_matrix[j][i + 1:]

        sign = (-1) ** i
        det += sign * matrix[0][i] * determinant(sub_matrix)

    return det
