#!/usr/bin/env python3
"""
module containing function deep_rnn
"""
import numpy as np


def deep_rnn(rnn_cells, X, h_0):
    """
    function that performs forward propagation for a deeep RNN
    Args:
        rnn_cells: list of RNNCell instances of length l
            that will be used for the forward propagation
            l: number of layers
        X: data to be used, given as a numpy.ndarray of shape (t, m, i)
            t: maximum number of time steps
            m: batch size
            i: dimensionality of the data
        h_0: initial hidden state, given as a numpy.ndarray of shape (l, m, h)
            h: dimensionality of the hidden state
    Return: H, Y
        H: numpy.ndarray containing all of the hidden states
        Y: numpy.ndarray containing all of the outputs
    """
    t = X.shape[0]
    m = X.shape[1]
    nb_layers = h_0.shape[0]
    h = h_0.shape[2]

    H = np.zeros(shape=(t + 1, nb_layers, m, h))
    Y = []
    H[0] = np.copy(h_0)

    for time_step in range(t):
        for layer in range(nb_layers):
            if layer == 0:
                h, y = rnn_cells[layer].forward(H[time_step][layer],
                                                X[time_step])
            else:
                h, y = rnn_cells[layer].forward(H[time_step][layer], h)
            H[time_step + 1][layer] = h

        Y.append(y)
    Y = np.array(Y)

    return H, Y
