#!/usr/bin/env python3
"""
module containing class GaussianProcess:
Class constructor: def __init__(self, X_init, Y_init, l=1, sigma_f=1)
Public instance method: def kernel(self, X1, X2):
"""
import numpy as np


class GaussianProcess:
    """
    Class GaussianProcess : represents a noiseless 1D Gaussian process
    """

    def __init__(self, X_init, Y_init, l=1, sigma_f=1):
        """
        Class contructor
        Args:
            X_init: numpy.ndarray of shape (t, 1)
                representing the inputs already sampled with the black-box
                function
            Y_init: numpy.ndarray of shape (t, 1)
                representing the outputs of the black-box function for each
                input in X_init
            t: number of initial samples
            l: length parameter for the kernel
            sigma_f: standard deviation given to the output of the black-box
                function
        Public instance attributes:
            X, Y, l and sigma_f: corresponding to the respective constructor
                inputs
            K: representing the current covariance kernel matrix for the
                Gaussian process
        """
        self.X = X_init
        self.Y = Y_init
        self.l = l
        self.sigma_f = sigma_f
        self.K = self.kernel(X_init, X_init)

    def kernel(self, X1, X2):
        """
        Public instance method that calculates the covariance kernel matrix
            between two matrices
        Args:
            X1: numpy.ndarray of shape (m, 1)
            X2: numpy.ndarray of shape (n, 1)
        Returns the covariance kernel matrix as a numpy.ndarray of shape (m, n)
            RBF kernel: K(Xi, Xj) = sigma_f² * exp(-1/2l² * (Xi-Xj)T * (Xi-Xj))
        """
        sigma_f = self.sigma_f
        l = self.l
        sqdist = np.sum(X1 ** 2, axis=1).reshape(-1, 1) + \
            np.sum(X2 ** 2, axis=1) - 2 * np.dot(X1, X2.T)
        exponent = -0.5 * sqdist / (l ** 2)
        K = sigma_f ** 2 * np.exp(exponent)
        return K
