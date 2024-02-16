#!/usr/bin/env python3
"""
module containing function initialize for GMM clustering method
"""
import numpy as np
kmeans = __import__('1-kmeans').kmeans


def initialize(X, k):
    """
    function that initializes variables for a Gaussian Mixture Model
    Args:
        X: numpy.ndarray of shape (n, d) containing the dataset
            n is the number of data points
            d is the number of dimensions in each data point
        k: positive integer containing the number of clusters
    Return: pi, m, S, or None, None, None on failure
        pi: numpy.ndarray of shape (k,) containing the priors for each cluster
        m: numpy.ndarray of shape (k, d) containing the centroid means for each
            cluster, initialized with K-means
        S: numpy.ndarray of shape (k, d, d) containing the covariance matrices
            for each cluster, initialized as identity matrices
    """
    if type(X) != np.ndarray or len(X.shape) != 2:
        return None, None, None
    if type(k) != int or k <= 0:
        return None, None, None

    try:
        prior = 1 / k
        pi = np.full(shape=(k,), fill_value=prior)

        m = kmeans(X, k)[0]

        d = m.shape[1]
        S = np.full(shape=(k, d, d), fill_value=np.identity(d))

        return pi, m, S

    except Exception:
        return None, None, None
