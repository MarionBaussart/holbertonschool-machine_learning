#!/usr/bin/env python3
"""
module containing function likelihood
"""
import numpy as np


def likelihood(x, n, P):
    """
    function that calculates the likelihood
    Args:
        x: number of patients that develop severe side effects
        n: total number of patients observed
        P: 1D numpy.ndarray containing the various hypothetical
            probabilities of developing severe side effects
    Return: 1D numpy.ndarray containing the likelihood of obtaining the data,
        x and n, for each probability in P
        L(P | x, n) = (n x) p**x (1 - p)**(n - x)
        with (n x) = n! / (x! (n - x)!)
    """
    if type(n) != int or n <= 0:
        raise ValueError('n must be a positive integer')
    if type(x) != int or x < 0:
        raise ValueError(
            'x must be an integer that is greater than or equal to 0')
    if x > n:
        raise ValueError('x cannot be greater than n')
    if type(P) != np.ndarray or len(P.shape) != 1:
        raise TypeError('P must be a 1D numpy.ndarray')

    valueerror = 0
    for proba in P:
        if proba < 0 or proba > 1:
            valueerror = 1
    if valueerror == 1:
        raise ValueError('All values in P must be in the range [0, 1]')

    likelihood = []

    x_parmi_n = np.math.factorial(n) / (
        np.math.factorial(x) * np.math.factorial(n - x))
    likelihood = x_parmi_n * (P ** x) * ((1 - P) ** (n - x))

    return likelihood
