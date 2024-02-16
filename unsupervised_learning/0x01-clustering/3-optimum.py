#!/usr/bin/env python3
"""
module containing function optimum_k
"""
import numpy as np
kmeans = __import__('1-kmeans').kmeans
variance = __import__('2-variance').variance


def optimum_k(X, kmin=1, kmax=None, iterations=1000):
    """
    function that tests for the optimum number of clusters by variance
    Args:
        X: numpy.ndarray of shape (n, d) containing the dataset
            n is the number of data points
            d is the number of dimensions in each data point
        kmin: positive integer containing the minimum number of clusters
            to check for (inclusive)
        kmax: positive integer containing the maximum number of clusters
        iterations: positive integer containing the maximum number of
            iterations for K-means
    Return: results, d_vars, or None on failure
        results: list containing the outputs of K-means for each cluster size
        d_vars: list containing the difference in variance from the smallest
            cluster size
    """
    if type(X) != np.ndarray or len(X.shape) != 2:
        return None, None
    if type(kmin) != int or kmin < 1:
        return None, None
    if kmax is None:
        kmax = X.shape[0]
    if type(kmax) != int or kmax < 1:
        return None, None
    if kmax <= kmin:
        return None, None
    if type(iterations) != int or iterations < 1:
        return None, None

    try:
        results = []
        var = []

        for k in range(kmin, kmax + 1):
            C, clss = kmeans(X, k, iterations)
            results.append((C, clss))
            var.append((variance(X, C)))

        first_variance = var[0]
        d_vars = [first_variance - v for v in var]

        return results, d_vars

    except Exception:
        return None, None
