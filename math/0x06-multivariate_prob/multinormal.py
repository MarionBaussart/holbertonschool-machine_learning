#!/usr/bin/env python3
"""
module containing class MultiNormal
"""
import numpy as np


class MultiNormal:
    """
    Class MultiNormal : represents a Multivariate Normal distribution
    """

    def __init__(self, data):
        """
        Class contructor
        Args:
            data: numpy.ndarray of shape (d, n) containing the data set:
                n is the number of data points
                d is the number of dimensions in each data point
        """
        if type(data) != np.ndarray:
            raise TypeError('data must be a 2D numpy.ndarray')
        if len(data.shape) != 2:
            raise TypeError('data must be a 2D numpy.ndarray')
        if data.shape[1] < 2:
            raise ValueError('data must contain multiple data points')

        n = data.shape[1]
        d = data.shape[0]

        mean = np.mean(data.T, axis=0)
        mean = np.reshape(mean, newshape=(1, d))

        cov = np.matmul(data, data.T - mean) / (n - 1)

        self.mean = mean.T
        self.cov = cov.T

    def pdf(self, x):
        """
        Public instance method that calculates the PDF at a data point
        Args:
            x: numpy.ndarray of shape (d, 1) containing the data point whose
                PDF should be calculated
        Return:
            value of the PDF
        """
        d = self.mean.shape[0]

        if type(x) != np.ndarray:
            raise TypeError('x must be a numpy.ndarray')
        if len(x.shape) != 2 or x.shape[1] != 1 or x.shape[0] != d:
            raise ValueError('x must have the shape ({}, 1)'.format(d))

        xm = x - self.mean
        exponent = - 0.5 * np.matmul(xm.T, np.matmul(
            np.linalg.inv(self.cov), xm))
        pdf = np.exp(exponent[0][0]) / np.sqrt(
            ((2 * np.pi) ** d) * np.linalg.det(self.cov))

        return pdf
