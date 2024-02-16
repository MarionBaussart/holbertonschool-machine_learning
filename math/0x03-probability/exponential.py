#!/usr/bin/env python3
"""module containing class Exponential"""
e = 2.7182818285


class Exponential:
    """
    Class Exponential : represents an exponential distribution
    """

    def __init__(self, data=None, lambtha=1.):
        """
        Class contructor
        Args:
            data: list of the data to be used to estimate the distribution
            lambtha: instance attribute, expected number of occurences
            in a given time frame
        """
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            else:
                self.lambtha = float(lambtha)
        else:
            if type(data) != list:
                raise TypeError("data must be a list")
            elif len(data) < 2:
                raise ValueError("data must contain multiple values")
            else:
                mean = sum(data) / len(data)
                self.lambtha = float(1 / mean)

    def pdf(self, x):
        """
        Instance method that calculate the PDF
        for a given time period
        PDF = lambda * exp(-lambda * x)
        Args:
            x: the time period
        Return:
            the PDF value for x, 0 if x is out of range
        """
        if x < 0:
            return 0

        pdf = self.lambtha * (e ** (- self.lambtha * x))

        return pdf

    def cdf(self, x):
        """
        Instance method that calculate the CDF for a given time period
        CDF = 1 - (exp(-lambda * x))
        Args:
            x: the time period
        Return:
            the CDF value for x
        """
        if x < 0:
            return 0

        cdf = 1 - (e ** (- self.lambtha * x))

        return cdf
