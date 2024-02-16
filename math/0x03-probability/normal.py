#!/usr/bin/env python3
"""module containing class Normal"""
e = 2.7182818285
π = 3.1415926536


class Normal:
    """
    Class Normal : represents an normal distribution
    """

    def __init__(self, data=None, mean=0., stddev=1.):
        """
        Class contructor
        Args:
            data: list of the data to be used to estimate the distribution
            mean: the mean of the distribution (mu)
            stddev: the standard deviation of the distribution (sigma)
                stddev = sqrt(Somme(x - mean)² / effectif)
        """
        if data is None:
            if stddev <= 0:
                raise ValueError("stddev must be a positive value")
            else:
                self.mean = float(mean)
                self.stddev = float(stddev)
        else:
            if type(data) != list:
                raise TypeError("data must be a list")
            elif len(data) < 2:
                raise ValueError("data must contain multiple values")
            else:
                self.mean = float(sum(data) / len(data))
                stddev_term = 0
                for i in range(len(data)):
                    stddev_term += (data[i] - self.mean) ** 2
                self.stddev = float((stddev_term / len(data)) ** (1 / 2))

    def z_score(self, x):
        """
        Instance method that calculate z-score of a given x-value
            z-score: number of stddev from the mean
        Args:
            x: the x-value
        Return:
            the z-score of x
        """
        return (x - self.mean) / self.stddev

    def x_value(self, z):
        """
        Instance method that calculate x-value of a given z-score
            z-score: number of stddev from the mean
        Args:
            z is the z-score
        Return:
            the x-value of z
        """
        return (z * self.stddev) + self.mean

    def pdf(self, x):
        """
        Instance method that calculate the value of the PDF for a given x-value
            PDF = 1/sqrt(2π*sigma²) * exp(-1/2((x - m)²/sigma²))
        Args:
            x: the x-value
        Return:
            the PDF value for x
        """
        racine = (2 * π * self.stddev ** 2) ** (- 1 / 2)
        exponent = (- 1 / 2) * (((x - self.mean) ** 2) / (self.stddev ** 2))
        return racine * (e ** (exponent))

    def cdf(self, x):
        """
        Instance method that calculate the value of the CDF
        for a given time period
            CDF = 1/2 + 1/2erf((x-mean)/(sqrt(2)*sigma))
        Args:
            x: the x-value
        Return:
            the CDF value for x
        """
        arg = (x - self.mean) / (self.stddev * (2 ** (1 / 2)))
        factor = 2 / (π ** (1 / 2))
        integral = (arg -
                    ((arg ** 3) / 3) +
                    ((arg ** 5) / 10) -
                    ((arg ** 7) / 42) +
                    ((arg ** 9) / 216))
        erf = factor * integral

        cdf = (1 / 2) * (1 + erf)

        return cdf
