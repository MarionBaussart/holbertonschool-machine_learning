#!/usr/bin/env python3
"""
module containing function viterbi
"""
import numpy as np


def viterbi(Observation, Emission, Transition, Initial):
    """
    function that calculates the most likely sequence of hidden states for a
        hidden markov model
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
    Return: path, P, or None, None on failure
        path: list of length T containing the most likely sequence of hidden
            states
        P: probability of obtaining the path sequence
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

    V = np.zeros(shape=(N, T))
    V[:, 0] = Initial.T * Emission[:, Observation[0]]

    prev = np.zeros(shape=(N, T - 1))

    for t in range(1, T):
        for j in range(N):
            proba = V[:, t - 1] * Transition[:, j] * Emission[
                j, Observation[t]]
            prev[j, t - 1] = np.argmax(proba)
            V[j, t] = np.max(proba)

    S = np.zeros(T)
    last_state = np.argmax(V[:, T - 1])
    S[0] = last_state

    backtrack_index = 1
    for i in range(T - 2, -1, -1):
        S[backtrack_index] = prev[int(last_state), i]
        last_state = prev[int(last_state), i]
        backtrack_index += 1

    S = np.flip(S, axis=0)

    path = []
    for s in S:
        path.append(int(s))

    P = np.amax(V, axis=0)
    P = np.amin(P)

    return path, P
