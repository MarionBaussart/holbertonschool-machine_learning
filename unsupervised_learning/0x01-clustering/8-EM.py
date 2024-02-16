#!/usr/bin/env python3
"""
module containing function expectation_maximization
"""
import numpy as np
initialize = __import__('4-initialize').initialize
expectation = __import__('6-expectation').expectation
maximization = __import__('7-maximization').maximization


def expectation_maximization(X, k, iterations=1000, tol=1e-5, verbose=False):
    """
    function that performs the expectation maximization for a GMM
    Args:
        X: numpy.ndarray of shape (n, d) containing the data set
            n: number of data points
            d: number of dimensions for each data point
        k: positive integer containing the number of clusters
        iterations: positive integer containing the maximum number of
            iterations for the algorithm
        tol: non-negative float containing tolerance of the log likelihood,
            used to determine early stopping i.e. if the difference is less
            than or equal to tol you should stop the algorithm
        verbose: boolean that determines if you should print information about
            the algorithm
    Return: pi, m, S, g, l, or None, None, None, None, None on failure
        pi: numpy.ndarray of shape (k,) containing the priors for each cluster
        m: numpy.ndarray of shape (k, d) containing the centroid means for each
            cluster
        S: numpy.ndarray of shape (k, d, d) containing the covariance matrices
            for each cluster
        g: numpy.ndarray of shape (k, n) containing the probabilities for each
            data point in each cluster
        l: the log likelihood of the model
    """
    if type(X) != np.ndarray or len(X.shape) != 2:
        return None, None, None, None, None
    if type(k) != int or k <= 0:
        return None, None, None, None, None
    if type(iterations) != int or iterations < 1:
        return None, None, None, None, None
    if type(tol) != float or tol < 0:
        return None, None, None, None, None
    if type(verbose) != bool:
        return None, None, None, None, None

    pi, m, S = initialize(X, k)
    log_likelihood_initial = 0
    i = 0

    while i < iterations:
        g, log_likelihood = expectation(X, pi, m, S)

        if verbose and i % 10 == 0:
            print("Log Likelihood after {} iterations: {}".format(
                i, round(log_likelihood, 5)))

        if abs(log_likelihood - log_likelihood_initial) <= tol:
            break

        pi, m, S = maximization(X, g)
        log_likelihood_initial = log_likelihood
        i += 1

    g, log_likelihood = expectation(X, pi, m, S)

    if verbose:
        print("Log Likelihood after {} iterations: {}".format(
            i, round(log_likelihood, 5)))

    return pi, m, S, g, log_likelihood
