#!/usr/bin/env python3
"""
module containing function mean_cov
"""
import numpy as np


def mean_cov(X):
    """
    function that calculates the mean and covariance of a data set
    Args:
        X: numpy.ndarray of shape (n, d)
            containing the data set:
                n is the number of data points
                d is the number of dimensions in each data point
    Return: mean, cov
        mean: numpy.ndarray of shape (1, d)
            containing the mean of the data set
        cov: numpy.ndarray of shape (d, d)
            containing the covariance matrix of the data set
    """
    if type(X) != np.ndarray:
        raise TypeError('X must be a 2D numpy.ndarray')
    if len(X.shape) != 2:
        raise TypeError('X must be a 2D numpy.ndarray')
    if X.shape[0] < 2:
        raise ValueError('X must contain multiple data points')

    n = X.shape[0]
    d = X.shape[1]

    mean = np.mean(X, axis=0)
    mean = np.reshape(mean, newshape=(1, d))

    cov = np.matmul(X.T, X - mean) / (n - 1)

    return mean, cov
