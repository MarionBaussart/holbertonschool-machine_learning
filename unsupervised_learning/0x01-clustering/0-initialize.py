#!/usr/bin/env python3
"""
module containing function initialize
"""
import numpy as np


def initialize(X, k):
    """
    function that initializes cluster centroids for K-means
    Args:
        X: numpy.ndarray of shape (n, d)
            containing the dataset that will be used for K-means clustering
                n is the number of data points
                d is the number of dimensions in each data point
        k: positive integer containing the number of clusters
    Return: numpy.ndarray of shape (k, d) containing the initialized centroids
        for each cluster, or None on failure
    """
    if type(k) != int or k <= 0:
        return None

    try:
        minimum = np.min(X, axis=0)
        maximum = np.max(X, axis=0)

        initialized_centroids = np.random.uniform(low=minimum,
                                                  high=maximum,
                                                  size=(k, X.shape[1]))

        return initialized_centroids

    except Exception:
        return None
