#!/usr/bin/env python3
"""script that performs matrix multiplication"""


def mat_mul(mat1, mat2):
    """function that performs matrix multiplication
        Args:
            matrices to multiplicate
        Return:
            the multiplication in new matrix,
            None if matrices cannot be multiplicated
    """
    # multiplication possible if nbcolumns mat1 = nblines mat2
    if len(mat1[0]) == len(mat2):
        # result matrix has same columns as mat2, same line as mat1
        result = [[0] * len(mat2[0]) for i in range(len(mat1))]
        for i in range(len(mat1)):
            for j in range(len(mat2[0])):
                for k in range(len(mat2)):
                    result[i][j] += mat1[i][k] * mat2[k][j]
        return result
    else:
        return None
