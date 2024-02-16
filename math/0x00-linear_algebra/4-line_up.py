#!/usr/bin/env python3
"""script that adds two arrays"""


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
