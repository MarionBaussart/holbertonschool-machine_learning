#!/usr/bin/env python3
"""
module containing function regular
"""
import numpy as np


def regular(P):
    """
    function that determines the steady state probabilities
        of a regular markov chain
    Args:
        P: square 2D numpy.ndarray of shape (n, n)
            representing the transition matrix
            P[i, j]: probability of transitioning from state i to state j
            n: number of states in the markov chain
    Return: numpy.ndarray of shape (1, n) containing the steady state
        probabilities, or None on failure
    """
    if type(P) != np.ndarray or len(P.shape) != 2 or P.shape[0] != P.shape[1]:
        return None
    if not (np.all(P >= 0) and np.all(P <= 1)):
        return None
    if not (np.all(np.sum(P, axis=1) == 1)):
        return None
    if P.shape[0] < 1:
        return None

    # check if the matrix is regular:
    if not np.all(np.matmul(P, P) > 0):
        return None

    try:
        P_transpose = P.T
        eigenvalues, eigenvectors = np.linalg.eig(P_transpose)
        index_close_1 = np.isclose(eigenvalues, 1)
        target_eigenvectors = eigenvectors[:, index_close_1]
        target_eigenvectors = target_eigenvectors[:, 0]

        steady_state = target_eigenvectors / np.sum(target_eigenvectors)
        steady_state = np.reshape(steady_state,
                                  newshape=(1, steady_state.shape[0]))

        return steady_state

    except Exception:
        return None
