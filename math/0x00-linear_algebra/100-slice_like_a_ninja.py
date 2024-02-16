#!/usr/bin/env python3trans
"""script that slices a matrix along specific axes"""


def np_slice(matrix, axes={}):
    """function that slices a matrix along specific axes
        Args:
            matrix to slice
        Return:
            a new numpy.ndarray sliced
    """
    new_matrix = matrix
    list_slice = []
    for key in range((max(axes.keys()) + 1)):
        value = axes.get(key)
        if value:
            list_slice.append(slice(*value))
        else:
            list_slice.append(slice(None))
    tuple_slice = tuple(list_slice)
    return new_matrix[tuple_slice]
