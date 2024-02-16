#!/usr/bin/env python3
"""
module containing function likelihood, intersection, marginal
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
    if np.any(P < 0) or np.any(P > 1):
        raise ValueError('All values in P must be in the range [0, 1]')

    likelihood = []

    x_parmi_n = np.math.factorial(n) / (
        np.math.factorial(x) * np.math.factorial(n - x))
    likelihood = x_parmi_n * (P ** x) * ((1 - P) ** (n - x))

    return likelihood


def intersection(x, n, P, Pr):
    """
    function that calculates the intersection of obtaining this data
        with the various hypothetical probabilities
    Args:
        x: number of patients that develop severe side effects
        n: total number of patients observed
        P: 1D numpy.ndarray containing the various hypothetical
            probabilities of developing severe side effects
        Pr: 1D numpy.ndarray containing the prior beliefs of P
    Return: 1D numpy.ndarray containing the intersection of obtaining x and n
        with each probability in P
        P(A inter B) = likelihood * prior
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
    if type(Pr) != np.ndarray or P.shape != Pr.shape:
        raise TypeError('Pr must be a numpy.ndarray with the same shape as P')
    if np.any(P < 0) or np.any(P > 1):
        raise ValueError('All values in P must be in the range [0, 1]')
    if np.any(Pr < 0) or np.any(Pr > 1):
        raise ValueError('All values in P must be in the range [0, 1]')
    if not np.isclose(np.sum(Pr), 1):
        raise ValueError('Pr must sum to 1')

    intersection = []

    intersection = likelihood(x, n, P) * Pr

    return intersection


def marginal(x, n, P, Pr):
    """
    function that calculates the marginal probability of obtaining the data
    Args:
        x: number of patients that develop severe side effects
        n: total number of patients observed
        P: 1D numpy.ndarray containing the various hypothetical
            probabilities of developing severe side effects
        Pr: 1D numpy.ndarray containing the prior beliefs of P
    Return: the marginal probability of obtaining x and n
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
    if type(Pr) != np.ndarray or P.shape != Pr.shape:
        raise TypeError('Pr must be a numpy.ndarray with the same shape as P')
    if np.any(P < 0) or np.any(P > 1):
        raise ValueError('All values in P must be in the range [0, 1]')
    if np.any(Pr < 0) or np.any(Pr > 1):
        raise ValueError('All values in Pr must be in the range [0, 1]')
    if not np.isclose(np.sum(Pr), 1):
        raise ValueError('Pr must sum to 1')

    intersection = likelihood(x, n, P) * Pr
    marginal = np.sum(intersection)

    return marginal
