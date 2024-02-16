#!/usr/bin/env python3
"""
module containing function BIC
"""
import numpy as np
expectation_maximization = __import__('8-EM').expectation_maximization


def BIC(X, kmin=1, kmax=None, iterations=1000, tol=1e-5, verbose=False):
    """
    function that finds the best number of clusters for a GMM
        using the Bayesian Information Criterion
    Args:
        X: numpy.ndarray of shape (n, d) containing the data set
            n: number of data points
            d: number of dimensions for each data point
        kmin: positive integer containing the minimum number of clusters to
            check for (inclusive)
        kmax: positive integer containing the maximum number of clusters to
            check for (inclusive)
        iterations: positive integer containing the maximum number of
            iterations for the algorithm
        tol: non-negative float containing the tolerance for the EM algorithm
        verbose: boolean that determines if the EM algorithm should print
            information to the standard output
    Return: best_k, best_result, l, b, or None, None, None, None on failure
        best_k: best value for k based on its BIC
        best_result: tuple containing pi, m, S
            pi: numpy.ndarray of shape (k,) containing the cluster priors for
                the best number of clusters
            m: numpy.ndarray of shape (k, d) containing the centroid means for
                the best number of clusters
            S: numpy.ndarray of shape (k, d, d) containing the covariance
                matrices for the best number of clusters
        l: numpy.ndarray of shape (kmax - kmin + 1) containing the log
            likelihood for each cluster size tested
        b: numpy.ndarray of shape (kmax - kmin + 1) containing the BIC value
            for each cluster size tested
        BIC = p * ln(n) - 2 * l
            p: number of parameters required for the model :
                number-of-parameters-to-be-learned-in-k-guassian-mixture-model
            n: number of data points used to create the model
            l: log likelihood of the model
    """
    if type(X) != np.ndarray or len(X.shape) != 2:
        return None, None, None, None
    if type(kmin) != int or kmin < 1:
        return None, None, None, None
    if kmax is None:
        kmax = X.shape[0]
    if type(kmax) != int or kmax < 1:
        return None, None, None, None
    if kmax <= kmin:
        return None, None, None, None
    if type(iterations) != int or iterations < 1:
        return None, None, None, None
    if type(tol) != float or tol < 0:
        return None, None, None, None
    if type(verbose) != bool:
        return None, None, None, None

    n, d = X.shape
    k_values_list = []
    results_list = []
    log_likelihood_list = []
    bic_value_list = []

    for k in range(kmin, kmax + 1):
        pi, m, S, _, log_likelihood = expectation_maximization(
            X, k, iterations, tol, verbose)

        p = d * k + (d * k * (d + 1) / 2) + k - 1
        BIC = p * np.log(n) - 2 * log_likelihood

        k_values_list.append(k)
        results_list.append((pi, m, S))
        log_likelihood_list.append(log_likelihood)
        bic_value_list.append(BIC)

        log_likelihood_array = np.array(log_likelihood_list)
        bic_value_array = np.array(bic_value_list)
        index = np.argmin(bic_value_array)

        best_k = k_values_list[index]
        best_result = results_list[index]

    return best_k, best_result, log_likelihood_array, bic_value_array
