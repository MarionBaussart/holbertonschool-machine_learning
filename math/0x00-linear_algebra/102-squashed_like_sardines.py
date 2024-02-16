#!/usr/bin/env python3
"""in test, script that concatenates two matrices along a specific axis"""


def cat_matrices(mat1, mat2, axis=0):
    """function that concatenates two matrices along a specific axis
        Args:
            matrices to concatenate
            axis
        Return:
            the concatenated matrix, None if matrices cannot be concatenated
    """
    matrix = []

    # axis 0
    if axis == 0:
        matrix.extend(mat1)
        matrix.extend(mat2)
        return matrix

    # axis 1
    else:
        for i in range(axis):

            matrix.insert(len(mat1[0]), cat_matrices(mat1[i], mat2[i]))
            if len(mat1[i]) == len(mat2[i]):
                matrix.append(mat1[i+1])
                matrix[i+1].extend(mat2[i+1])
            else:
                return None
        return matrix

    # axis more than 1

