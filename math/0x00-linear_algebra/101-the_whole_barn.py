#!/usr/bin/env python3
"""script that adds two matrices"""
import numpy as np


def add_matrices(mat1, mat2):
    """function that adds two matrices
        Args:
            matrices to add
        Return:
            the addition, None if matrices are of different shape
    """
    matrice1 = np.array(mat1.copy())
    matrice2 = np.array(mat2.copy())
    if matrice1.shape == matrice2.shape:
        sum = np.add(matrice1, matrice2)
        return sum
    else:
        return None
