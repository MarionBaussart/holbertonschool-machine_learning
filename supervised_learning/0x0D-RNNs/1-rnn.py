#!/usr/bin/env python3
"""
module containing function rnn
"""
import numpy as np


def rnn(rnn_cell, X, h_0):
    """
    function that performs forward propagation for a simple RNN
    Args:
        rnn_cell: instance of RNNCell that will be used for the forward
            propagation
        X: data to be used, given as a numpy.ndarray of shape (t, m, i)
            t: maximum number of time steps
            m: batch size
            i: dimensionality of the data
        h_0: initial hidden state, given as a numpy.ndarray of shape (m, h)
            h: dimensionality of the hidden state
    Return: H, Y
        H: numpy.ndarray containing all of the hidden states
        Y: numpy.ndarray containing all of the outputs
    """
    t = X.shape[0]
    m = X.shape[1]
    h = h_0.shape[1]
    o = rnn_cell.by.shape[1]

    H = np.zeros(shape=(t + 1, m, h))
    Y = np.zeros(shape=(t, m, o))
    H[0] = np.copy(h_0)

    for time_step in range(t):
        H[time_step + 1], Y[time_step] = rnn_cell.forward(
            H[time_step], X[time_step])

    return H, Y
