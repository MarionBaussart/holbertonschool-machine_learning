#!/usr/bin/env python3
"""script that concatenates two matrices along a specific axis"""


def cat_matrices2D(mat1, mat2, axis=0):
    """function that concatenates two matrices along a specific axis
        Args:
            matrices to concatenate
            axis, 0 if you add on a new line, 1 on a new column
        Return:
            the concatenation in new matrix,
            None if matrices cannot be concatenated
    """
    for element in mat1:
        if len(element) != len(mat1[0]):
            return None
    for element in mat2:
        if len(element) != len(mat2[0]):
            return None

    # add on a new line
    if axis == 0 and len(mat1[0]) == len(mat2[0]):
        result = []
        result.extend(mat1)
        result.extend(mat2)
        return result

    # add on a new column
    elif axis == 1 and len(mat1) == len(mat2):
        result = [mat1[i] + mat2[i] for i in range(len(mat1))]
        return result

    # if matrices can't be concatened
    else:
        return None
