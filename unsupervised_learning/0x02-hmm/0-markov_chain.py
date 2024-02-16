#!/usr/bin/env python3
"""
module containing function markov_chain
"""
import numpy as np


def markov_chain(P, s, t=1):
    """
    function that determines the probability of a markov chain being in a
        particular state after a specified number of iterations
    Args:
        P: square 2D numpy.ndarray of shape (n, n)
            representing the transition matrix
            P[i, j]: probability of transitioning from state i to state j
            n: number of states in the markov chain
        s: numpy.ndarray of shape (1, n)
            representing the probability of starting in each state
        t: number of iterations that the markov chain has been through
    Return: numpy.ndarray of shape (1, n) representing the probability of being
        in a specific state after t iterations, or None on failure
    """
    if type(P) != np.ndarray or len(P.shape) != 2 or P.shape[0] != P.shape[1]:
        return None
    if not (np.all(P >= 0) and np.all(P <= 1)):
        return None
    if P.shape[0] <= 1:
        return None

    if type(s) != np.ndarray or len(s.shape) != 2 or s.shape[0] != 1\
            or s.shape[1] != P.shape[0]:
        return None
    if not (np.all(s >= 0) and np.all(s <= 1)):
        return None

    if type(t) != int or t <= 0:
        return None

    try:
        s_t = np.matmul(s, np.linalg.matrix_power(P, t))
        return s_t

    except Exception:
        return None
