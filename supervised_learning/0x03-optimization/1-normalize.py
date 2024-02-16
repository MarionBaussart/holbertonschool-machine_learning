#!/usr/bin/env python3
"""
module containing function normalize
"""


def normalize(X, m, s):
    """
    function that normalizes (standardizes) a matrix
    Args:
        X: the numpy.ndarray of shape (d, nx) to normalize
            with d: the number of data points
            nx: the number of features
        m: numpy.ndarray of shape (nx,) that contains the mean
            of all features of X
        s: numpy.ndarray of shape (nx,) that contains the standard deviation
            of all features of X
    Return: the normalized X matrix
    """
    normalized_X = (X - m) / s

    return normalized_X
