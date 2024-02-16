#!/usr/bin/env python3
"""
module containing function pca
"""
import numpy as np


def pca(X, ndim):
    """
    function that performs PCA on a dataset
    Args:
        X: numpy.ndarray of shape (n, d)
            containing the data set:
                n is the number of data points
                d is the number of dimensions in each data point
        ndim: new dimensionality of the transformed X
    Return: T, a numpy.ndarray of shape (n, ndim)
        containing the transformed version of X
    """
    X = X - np.mean(X, axis=0)
    U, S, V = np.linalg.svd(X)

    W = V.T[:, :ndim]
    T = np.matmul(X, W)

    return T
