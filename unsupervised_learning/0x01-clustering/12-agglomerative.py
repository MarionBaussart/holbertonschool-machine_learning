#!/usr/bin/env python3
"""
module containing function agglomerative
"""
import scipy.cluster.hierarchy
import matplotlib.pyplot as plt


def agglomerative(X, dist):
    """
    function that performs agglomerative clustering on a dataset
    Args:
        X: numpy.ndarray of shape (n, d) containing the dataset
        dist: maximum cophenetic distance for all clusters
    Return: 
        clss: numpy.ndarray of shape (n,) containing the cluster indices
            for each data point
    """
    Z = scipy.cluster.hierarchy.linkage(X, method="ward")
    clss = scipy.cluster.hierarchy.fcluster(Z, t=dist, criterion="distance")
    dendogram = scipy.cluster.hierarchy.dendrogram(Z, color_threshold=dist)
    plt.show()

    return clss
