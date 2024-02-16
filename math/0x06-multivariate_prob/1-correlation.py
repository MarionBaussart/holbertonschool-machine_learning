#!/usr/bin/env python3
"""
module containing function correlation
"""
import numpy as np


def correlation(C):
    """
    function that calculates a correlation matrix
    Args:
        C: numpy.ndarray of shape (d, d) containing a covariance matrix
            d is the number of dimensions
    Return: numpy.ndarray of shape (d, d) containing the correlation matrix
    Co(x,y) = Cov(x,y)/(stddevx*stddevy) with stddev = sqrt(var)
    """
    if type(C) != np.ndarray:
        raise TypeError('C must be a numpy.ndarray')
    if len(C.shape) != 2 or C.shape[0] != C.shape[1]:
        raise ValueError('C must be a 2D square matrix')

    d = C.shape[0]
    Co = np.ndarray(shape=(d, d))

    for i in range(d):
        for j in range(d):
            Co[i][j] = C[i][j] / (np.sqrt(C[i][i]) * np.sqrt(C[j][j]))

    return Co
