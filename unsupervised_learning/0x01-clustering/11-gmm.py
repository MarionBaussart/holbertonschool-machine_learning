#!/usr/bin/env python3
"""
module containing function gmm
"""
import sklearn.mixture


def gmm(X, k):
    """
    function that calculates a GMM from a dataset
    Args:
        X: numpy.ndarray of shape (n, d) containing the dataset
        k: number of clusters
    Return: pi, m, S, clss, bic
        pi: numpy.ndarray of shape (k,) containing the cluster priors
        m: numpy.ndarray of shape (k, d) containing the centroid means
        S: numpy.ndarray of shape (k, d, d) containing the covariance matrices
        clss: numpy.ndarray of shape (n,) containing the cluster indices for
            each data point
        bic: numpy.ndarray of shape (kmax - kmin + 1) containing the BIC value
            for each cluster size tested
    """
    gaussian_mixture = sklearn.mixture.GaussianMixture(n_components=k).fit(X)
    pi = gaussian_mixture.weights_
    m = gaussian_mixture.means_
    S = gaussian_mixture.covariances_
    clss = gaussian_mixture.predict(X)
    bic = gaussian_mixture.bic(X)

    return pi, m, S, clss, bic
