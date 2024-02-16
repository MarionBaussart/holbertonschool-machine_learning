#!/usr/bin/env python3trans
"""script that concatenates two matrices along a specific axis"""
import numpy as np


def np_cat(mat1, mat2, axis=0):
    """function concatenates two matrices along a specific axis
        Args:
            matrices to concatenate
            axis, 0 if you add on a new line, 1 on a new column
        Return:
            the concatenation in new matrix
    """
    return np.concatenate((mat1, mat2), axis)
