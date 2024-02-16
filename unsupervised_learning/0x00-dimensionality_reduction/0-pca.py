#!/usr/bin/env python3
"""
module containing function pca
"""
import numpy as np


def pca(X, var=0.95):
    """
    function that performs PCA on a dataset
    Args:
        X: numpy.ndarray of shape (n, d)
            containing the data set:
                n is the number of data points
                d is the number of dimensions in each data point
                all dimensions have a mean of 0 across all data points
        var: fraction of the variance that the PCA transformation should
            maintain
    Return: the weights matrix, W, that maintains var fraction of X's original
        variance
            W: numpy.ndarray of shape (d, nd) where nd is the new
                dimensionality of the transformed X
    """
    U, S, V = np.linalg.svd(X)

    cumulated_sigma = np.cumsum(S)

    # search for new dimension with threshold = var(95%)
    for i in range(cumulated_sigma.shape[0]):
        fraction = cumulated_sigma[i] / cumulated_sigma[-1]
        if fraction >= var:
            nd = i + 1
            break

    W = V.T[:, :nd]

    return W
