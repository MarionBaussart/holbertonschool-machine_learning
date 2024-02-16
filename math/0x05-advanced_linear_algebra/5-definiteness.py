#!/usr/bin/env python3
"""
module containing function definiteness
"""
import numpy as np


def definiteness(matrix):
    """
    function that calculates the definiteness of a matrix
    Args:
        matrix: numpy.ndarray of shape (n, n) whose definiteness
            should be calculated
    Return: the definiteness of a matrix
    """
    if type(matrix) != np.ndarray:
        raise TypeError("matrix must be a numpy.ndarray")

    if len(matrix.shape) != 2 or matrix.shape[0] != matrix.shape[1]:
        return None

    if np.array_equal(matrix, matrix.T) is False:
        return None

    eigenvalues = [np.linalg.eigvals(matrix)]

    if np.all(eigenvalues[0] > 0):
        return("Positive definite")
    if np.all(eigenvalues[0] < 0):
        return("Negative definite")
    if np.all(eigenvalues[0] >= 0):
        return("Positive semi-definite")
    if np.all(eigenvalues[0] <= 0):
        return("Negative semi-definite")
    else:
        return("Indefinite")
