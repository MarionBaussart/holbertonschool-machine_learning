#!/usr/bin/env python3
"""
module containing function shuffle_data
"""
import numpy as np


def shuffle_data(X, Y):
    """
    function that shuffles the data points in two matrices the same way
    Args:
        X: the first numpy.ndarray of shape (m, nx) to shuffle
            m: the number of data points
            nx: the number of features in X
        Y: the second numpy.ndarray of shape (m, ny) to shuffle
            m: the same number of data points as in X
            ny: the number of features in Y
    Return: the shuffled X and Y matrices
    """
    permutation = np.random.permutation(X.shape[0])
    shuffled_X = X[permutation]
    shuffled_Y = Y[permutation]

    return shuffled_X, shuffled_Y
