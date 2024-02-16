#!/usr/bin/env python3
"""
module containing function maximization
"""
import numpy as np


def maximization(X, g):
    """
    function that calculates the maximization step in the EM algorithm
        for a GMM
    Args:
        X: numpy.ndarray of shape (n, d) containing the dataset
            n is the number of data points
            d is the number of dimensions in each data point
        g: numpy.ndarray of shape (k, n) containing the posterior probabilities
            for each data point in each cluster
    Return: pi, m, S, or None, None, None on failure
        pi: numpy.ndarray of shape (k,) containing the updated priors for each
            cluster
        m: numpy.ndarray of shape (k, d) containing the updated centroid means
            for each cluster
        S: numpy.ndarray of shape (k, d, d) containing the updated covariance
            matrices for each cluster
    """
    if type(X) != np.ndarray or len(X.shape) != 2:
        return None, None, None
    if type(g) != np.ndarray or len(g.shape) != 2:
        return None, None, None
    if X.shape[0] != g.shape[1]:
        return None, None, None
    if not np.isclose(np.sum(g, axis=0), 1).all():
        return None, None, None

    try:
        n, d = X.shape
        k = g.shape[0]

        pi = np.sum(g, axis=1) / n

        m = np.matmul(g, X) / np.sum(g, axis=1)[:, None]

        S = np.zeros(shape=(k, d, d))
        for cluster in range(k):
            xm = X - m[cluster]
            S[cluster] = np.sum(g[cluster, :, None, None] *
                                np.matmul(xm[:, :, None], xm[:, None, :]),
                                axis=0)
        S /= np.sum(g, axis=1)[:, None, None]

        return pi, m, S

    except Exception:
        return None, None
