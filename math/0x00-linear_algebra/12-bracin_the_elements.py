#!/usr/bin/env python3trans
"""script that performs element-wise addition, subtraction,
multiplication, and division"""


def np_elementwise(mat1, mat2):
    """function that performs element-wise addition, subtraction,
    multiplication, and division
        Args:
            matrices for the operations
        Return:
            tuple containing the element-wise sum, difference, product,
            and quotient
    """
    return (mat1 + mat2, mat1 - mat2, mat1 * mat2, mat1 / mat2)
