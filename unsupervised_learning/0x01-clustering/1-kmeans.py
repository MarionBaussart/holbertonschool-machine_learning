#!/usr/bin/env python3
"""
module containing function kmeans
"""
import numpy as np


def kmeans(X, k, iterations=1000):
    """
    function that performs K-means on a dataset
    Args:
        X: numpy.ndarray of shape (n, d)
            containing the dataset that will be used for K-means clustering
                n is the number of data points
                d is the number of dimensions in each data point
        k: positive integer containing the number of clusters
        iterations: positive integer containing the maximum number of
            iterations that should be performed
    Return: C, clss or None, None on failure
        C: numpy.ndarray of shape (k, d) containing the centroid means for each
            cluster
        clss: numpy.ndarray of shape (n,) containing the index of the cluster
            in C that each data point belongs to
    """
    if type(X) != np.ndarray or len(X.shape) != 2:
        return None, None

    if type(k) != int or k <= 0:
        return None, None

    if type(iterations) != int or iterations <= 0:
        return None, None

    try:
        minimum = np.min(X, axis=0)
        maximum = np.max(X, axis=0)

        C = np.random.uniform(low=minimum,
                              high=maximum,
                              size=(k, X.shape[1]))

        for i in range(iterations):
            centroids = np.copy(C)
            distances = np.linalg.norm(X - centroids[:, np.newaxis], axis=-1)
            clss = np.argmin(distances, axis=0)

            for cluster in range(k):
                if cluster not in clss:
                    C[cluster] = np.random.uniform(low=minimum,
                                                   high=maximum,
                                                   size=(1, X.shape[1]))
                else:
                    C[cluster] = np.mean(X[clss == cluster], axis=0)

            if np.all(centroids == C):
                return C, clss
            else:
                centroids = C

        distances = np.linalg.norm(X - centroids[:, np.newaxis], axis=-1)
        clss = np.argmin(distances, axis=0)

        return C, clss

    except Exception:
        return None, None
