#!/usr/bin/env python3
"""module containing class Poisson"""


class Poisson:
    """
    Class Poisson : represents a poisson distribution
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
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            else:
                mean = sum(data) / len(data)
                self.lambtha = float(mean)

    def pmf(self, k):
        """
        Instance method that calculate the PMF
        for a given number of “successes”
        PMF = (exp(-lambda) * lambda^k) / k!
        Args:
            k: the number of “successes”
        Return:
            the PMF value for k
        """
        if type(k) != int:
            k = int(k)
        if k < 0:
            return 0

        e = 2.7182818285
        k_factorial = 1
        for i in range(2, k + 1):
            k_factorial *= i
        pmf = ((e ** (- self.lambtha)) * (self.lambtha ** k)) / k_factorial

        return pmf

    def cdf(self, k):
        """
        Instance method that calculate the CDF
        for a given number of “successes”
        CDF = Somme(i=0 à k) de (exp(-lambda) * lambda^i) / i!
        Args:
            k: the number of “successes”
        Return:
            the CDF value for k
        """
        if type(k) != int:
            k = int(k)
        if k < 0:
            return 0

        cdf = 0
        for i in range(k + 1):
            cdf += self.pmf(i)

        return cdf
