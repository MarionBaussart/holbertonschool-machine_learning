#!/usr/bin/env python3
"""
module containing function initialize for GMM clustering method
"""
import numpy as np


def pdf(X, m, S):
    """
    function that calculates the probability density function of a Gaussian
        distribution
    Args:
        X: numpy.ndarray of shape (n, d) containing the dataset
            n is the number of data points
            d is the number of dimensions in each data point
        m: numpy.ndarray of shape (d,) containing the mean of the distribution
        S: numpy.ndarray of shape (d, d) containing the covariance of the
            distribution
    Return: P, or None on failure
        P: numpy.ndarray of shape (n,) containing the PDF values for each data
            point
    """
    if type(X) != np.ndarray or len(X.shape) != 2:
        return None
    d = X.shape[1]
    if type(m) != np.ndarray or len(m.shape) != 1 or m.shape[0] != d:
        return None
    if type(S) != np.ndarray or len(S.shape) != 2 or S.shape != (d, d):
        return None

    xm = X - m
    d = X.shape[1]
    det_cov = np.linalg.det(S)
    inverse_cov = np.linalg.inv(S)
    exponent = (- 1 / 2) * np.sum(
        xm * np.matmul(inverse_cov, xm.T).T, axis=1)

    pdf = (2 * np.pi) ** (- d / 2)
    pdf *= det_cov ** (- 1 / 2)
    pdf *= np.exp(exponent)

    pdf[pdf < 1e-300] = 1e-300

    return pdf
