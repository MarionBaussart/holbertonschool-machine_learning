#!/usr/bin/env python3
"""
module containing function batch_norm
"""
import numpy as np


def batch_norm(Z, gamma, beta, epsilon):
    """
    function that normalizes an unactivated output of a neural network
        using batch normalization
    Args:
        Z: a numpy.ndarray of shape (m, n) that should be normalized
            m: the number of data points
            n: the number of features in Z
        gamma: a numpy.ndarray of shape (1, n) containing the scales
            used for batch normalization
        beta: a numpy.ndarray of shape (1, n) containing the offsets
            used for batch normalization
        epsilon: a small number used to avoid division by zero
    Return: the normalized Z matrix
    Z_normalized = ((Z - mean_Z) / variance_Z) * gamma + beta
    """
    mean_Z = np.mean(Z, axis=0)
    variance_Z = np.var(Z, axis=0)
    Z_normalized = (Z - mean_Z) / ((variance_Z + epsilon) ** 0.5)

    return (gamma * Z_normalized) + beta
