#!/usr/bin/env python3
"""
module containing function forward
"""
import numpy as np


def forward(Observation, Emission, Transition, Initial):
    """
    function that performs the forward algorithm for a hidden markov model
    Args:
        Observation:numpy.ndarray of shape (T,)
            that contains the index of the observation
            with T: number of observations
        Emission: numpy.ndarray of shape (N, M)
            containing the emission probability of a specific observation
            given a hidden state
            Emission[i, j]: probability of observing j given the hidden state i
            N: number of hidden states
            M: number of all possible observations
        Transition: 2D numpy.ndarray of shape (N, N)
            containing the transition probabilities
            Transition[i, j]: probability of transitioning from the hidden
            state i to j
        Initial: numpy.ndarray of shape (N, 1)
            containing the probability of starting in a particular hidden state
    Return: P, F, or None, None on failure
        P: likelihood of the observations given the model
        F: numpy.ndarray of shape (N, T)
            containing the forward path probabilities
            F[i, j]: probability of being in hidden state i at time j
            given the previous observations
    """
    if type(Observation) != np.ndarray or len(Observation.shape) != 1:
        return None, None
    T = Observation.shape[0]
    if type(T) != int or T < 1:
        return None, None

    if type(Emission) != np.ndarray or len(Emission.shape) != 2:
        return None, None
    if not (np.all(Emission >= 0) and np.all(Emission <= 1)):
        return None, None
    N = Emission.shape[0]
    M = Emission.shape[1]
    if type(N) != int or N < 1 or type(M) != int or M < 1:
        return None, None

    if type(Transition) != np.ndarray or Transition.shape != (N, N):
        return None, None
    if not (np.all(Transition >= 0) and np.all(Transition <= 1)):
        return None, None

    if type(Initial) != np.ndarray or Initial.shape != (N, 1):
        return None, None
    if not (np.all(Initial >= 0) and np.all(Initial <= 1)):
        return None, None

    F = np.zeros(shape=(N, T))
    F[:, 0] = Initial.T * Emission[:, Observation[0]]

    for t in range(1, T):
        for j in range(N):
            F[j, t] = np.matmul(F[:, t - 1], Transition[:, j]) * Emission[
                j, Observation[t]]

    P = np.sum(F[:, -1])

    return P, F
