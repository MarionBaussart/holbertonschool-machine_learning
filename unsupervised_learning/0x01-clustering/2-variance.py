#!/usr/bin/env python3
"""
module containing function variance
"""
import numpy as np


def variance(X, C):
    """
    function that calculates the total intra-cluster variance for a data set
    Args:
        X: numpy.ndarray of shape (n, d) containing the dataset
            n is the number of data points
            d is the number of dimensions in each data point
        C: numpy.ndarray of shape (k, d) containing the centroid means
            for each cluster
    Return: the total variance, or None on failure
    """
    try:
        distances = np.square(X[:, None, :] - C[None, :, :]).sum(axis=-1)
        min_distances = np.min(distances, axis=1)
        total_variance = np.sum(min_distances)

        return total_variance

    except Exception:
        return None
