#!/usr/bin/env python3
"""script that adds two 2D matrices"""


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
