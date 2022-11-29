#!/usr/bin/env python3trans
"""script that performs element-wise addition, subtraction,
multiplication, and division"""
import numpy as np


def np_elementwise(mat1, mat2):
    """function that performs element-wise addition, subtraction,
    multiplication, and division
        Args:
            matrices for the operations
        Return:
            tuple containing the element-wise sum, difference, product,
            and quotient
    """
    return (np.add(mat1, mat2), np.subtract(mat1, mat2),
            np.multiply(mat1, mat2), np.divide(mat1, mat2))
