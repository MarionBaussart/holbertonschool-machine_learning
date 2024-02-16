#!/usr/bin/env python3
"""
module containing function bi_rnn
"""
import numpy as np


def bi_rnn(bi_cell, X, h_0, h_t):
    """
    function that performs forward propagation for a bidirectional RNN
    Args:
        bi_cell: instance of BidirectinalCell that will be used for the forward
            propagation
        X: data to be used, given as a numpy.ndarray of shape (t, m, i)
            t: maximum number of time steps
            m: batch size
            i: dimensionality of the data
        h_0: initial hidden state in the forward direction,
            given as a numpy.ndarray of shape (m, h)
            h: dimensionality of the hidden state
        h_t: initial hidden state in the backward direction,
            given as a numpy.ndarray of shape (m, h)
    Return: H, Y
        H: numpy.ndarray containing all of the concatenatedv hidden states
        Y: numpy.ndarray containing all of the outputs
    """
    t = X.shape[0]
    m = X.shape[1]
    h = h_0.shape[1]
    o = bi_cell.by.shape[1]

    Hf = np.zeros(shape=(t + 1, m, h))
    Hb = np.zeros(shape=(t + 1, m, h))
    Y = np.zeros(shape=(t, m, o))

    Hf[0] = h_0
    Hb[t] = h_t

    for time_step in range(t):
        Hf[time_step + 1] = bi_cell.forward(Hf[time_step], X[time_step])

    for time_step in range(t - 1, -1, -1):
        Hb[time_step] = bi_cell.backward(Hb[time_step + 1], X[time_step])

    H = np.concatenate((Hf[1:], Hb[:t]), axis=-1)

    Y = bi_cell.output(H)

    return H, Y
