#!/usr/bin/env python3
"""
module containing function likelihood, intersection, marginal and posterior
"""
from scipy import special


def posterior(x, n, p1, p2):
    """
    function that calculates the posterior probability
    Args:
        x: number of patients that develop severe side effects
        n: total number of patients observed
        p1: lower bound on the range
        p2: upper bound on the range
    Return: posterior probability that p is within the range [p1, p2]
        given x and n
    """
    if type(n) != int or n <= 0:
        raise ValueError('n must be a positive integer')
    if type(x) != int or x < 0:
        raise ValueError(
            'x must be an integer that is greater than or equal to 0')
    if x > n:
        raise ValueError('x cannot be greater than n')
    if type(p1) != float or p1 < 0 or p1 > 1:
        raise ValueError('p1 must be a float in the range [0, 1]')
    if type(p2) != float or p2 < 0 or p2 > 1:
        raise ValueError('p2 must be a float in the range [0, 1]')
    if p2 <= p1:
        raise ValueError('p2 must be greater than p1')

    alpha = x + 1
    beta = n - x + 1
    integral_p1 = special.btdtr(alpha, beta, p1)
    integral_p2 = special.btdtr(alpha, beta, p2)
    posterior = integral_p2 - integral_p1

    return posterior
