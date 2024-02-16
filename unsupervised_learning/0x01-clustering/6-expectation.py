#!/usr/bin/env python3
"""
module containing function expectation
"""
import numpy as np
pdf = __import__('5-pdf').pdf


def expectation(X, pi, m, S):
    """
    function that calculates the expectation step in the EM algorithm for a GMM
    Args:
        X: numpy.ndarray of shape (n, d) containing the dataset
            n is the number of data points
            d is the number of dimensions in each data point
        pi: numpy.ndarray of shape (k,) containing the priors for each cluster
        m: numpy.ndarray of shape (k, d) containing the centroid means
            for each cluster
        S: numpy.ndarray of shape (k, d, d) containing the covariance matrices
            for each cluster
    Return: g, l, or None, None on failure
        g: numpy.ndarray of shape (k, n) containing the posterior probabilities
            for each data point in each cluster
        l: total log likelihood
    """
    if type(X) != np.ndarray or len(X.shape) != 2:
        return None, None
    if type(pi) != np.ndarray or len(pi.shape) != 1 or not np.isclose(
            np.sum(pi), 1):
        return None, None
    if type(m) != np.ndarray or len(m.shape) != 2 or m.shape[0] != pi.shape[0]\
            or m.shape[1] != X.shape[1]:
        return None, None
    if type(S) != np.ndarray or len(S.shape) != 3 or S.shape[0] != pi.shape[0]\
            or S.shape[1] != m.shape[1] or S.shape[2] != m.shape[1]:
        return None, None

    try:
        k = pi.shape[0]
        n = X.shape[0]
        posterior = np.zeros(shape=(k, n))

        for cluster in range(k):
            prior = pi[cluster]
            p = pdf(X, m[cluster], S[cluster])
            posterior[cluster] = prior * p

        somme_prior_pdf = np.sum(posterior, axis=0)
        posterior /= somme_prior_pdf

        likelihood = np.sum(np.log(somme_prior_pdf))

        return posterior, likelihood

    except Exception:
        return None, None
