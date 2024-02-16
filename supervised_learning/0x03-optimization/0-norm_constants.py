#!/usr/bin/env python3
"""
module containing function normalization_constants
"""
import numpy as np


def normalization_constants(X):
    """
    function that calculates the normalization (standardization)
        constants of a matrix
    Args:
        X: the numpy.ndarray of shape (m, nx) to normalize
            with m: the number of data points
            nx: the number of features
    Return: the mean and standard deviation of each feature
    """
    mean = np.mean(X, axis=0)
    standard_deviation = np.std(X, axis=0)

    return mean, standard_deviation
