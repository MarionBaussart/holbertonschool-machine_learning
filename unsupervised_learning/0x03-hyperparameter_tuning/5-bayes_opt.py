#!/usr/bin/env python3
"""
module containing class BayesianOptimization:
Class constructor: def __init__(self, f, X_init, Y_init,
                                bounds, ac_samples, l=1,
                                sigma_f=1, xsi=0.01, minimize=True)
Public instance method:
    def acquisition(self)
    def optimize(self, iterations=100)
"""
import numpy as np
from scipy.stats import norm
GP = __import__('2-gp').GaussianProcess


class BayesianOptimization:
    """
    Class BayesianOptimization : performs Bayesian optimization on a noiseless
        1D Gaussian process
    """

    def __init__(self, f, X_init, Y_init, bounds, ac_samples,
                 l=1, sigma_f=1, xsi=0.01, minimize=True):
        """
        Class contructor
        Args:
            f: black-box function to be optimized
            X_init: numpy.ndarray of shape (t, 1)
                representing the inputs already sampled with the black-box
                function
            Y_init: numpy.ndarray of shape (t, 1)
                representing the outputs of the black-box function for each
                input in X_init
            t: number of initial samples
            bounds: tuple of (min, max)
                representing the bounds of the space in which to look for the
                optimal point
            ac_samples: number of samples that should be analyzed during
                acquisition
            l: length parameter for the kernel
            sigma_f: standard deviation given to the output of the black-box
                function
            xsi: exploration-exploitation factor for acquisition
            minimize: bool determining whether optimization should be performed
                for minimization (True) or maximization (False)
        Public instance attributes:
            f: the black-box function
            gp: an instance of the class GaussianProcess
            X_s: a numpy.ndarray of shape (ac_samples, 1)
                containing all acquisition sample points, evenly spaced between
                min and max
            xsi: the exploration-exploitation factor
            minimize: a bool for minimization versus maximization
        """
        self.f = f
        self.gp = GP(X_init, Y_init, l, sigma_f)
        self.X_s = np.linspace(start=bounds[0],
                               stop=bounds[1],
                               num=ac_samples).reshape(ac_samples, 1)
        self.xsi = xsi
        self.minimize = minimize

    def acquisition(self):
        """
        Public instance method that calculates the next best sample location
            uses the Expected Improvement acquisition function
        Returns:
            X_next, EI
                X_next: numpy.ndarray of shape (1,)
                    representing the next best sample point
                EI: numpy.ndarray of shape (ac_samples,)
                    containing the expected improvement of each potential
                    sample
        """
        mu, sigma = self.gp.predict(self.X_s)
        mu_sample, _ = self.gp.predict(self.gp.X)

        if self.minimize:
            mu_sample_opt = np.min(mu_sample)
            imp = (mu_sample_opt - mu - self.xsi)
        else:
            mu_sample_opt = np.max(mu_sample)
            imp = (mu - mu_sample_opt - self.xsi)

        with np.errstate(divide='ignore', invalid='ignore'):
            Z = imp / sigma
        ei = imp * norm.cdf(Z) + sigma * norm.pdf(Z)
        ei[sigma == 0.0] = 0.0

        X_next = self.X_s[np.argmax(ei)]

        return X_next, ei

    def optimize(self, iterations=100):
        """
        Public instance method that optimizes the black-box function
        Args:
            iterations: maximum number of iterations to perform
        Returns: X_opt, Y_opt
            X_opt: numpy.ndarray of shape (1,)
                representing the optimal point
            Y_opt: numpy.ndarray of shape (1,)
                representing the optimal function value
        """
        X_opt, Y_opt = 0, 0
        for _ in range(iterations):
            X_next, _ = self.acquisition()
            Y_next = self.f(X_next)

            if X_next in self.gp.X:
                self.gp.X = self.gp.X[:-1]
                break

            else:
                self.gp.update(X_next, Y_next)

                if self.minimize and Y_next < Y_opt:
                    X_opt = X_next
                    Y_opt = Y_next

                if not self.minimize and Y_next > Y_opt:
                    X_opt = X_next
                    Y_opt = Y_next

        return X_opt, Y_opt
