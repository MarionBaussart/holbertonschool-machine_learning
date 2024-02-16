#!/usr/bin/env python3
"""
module containing class GRUCell:
Class constructor: def __init__(self, i, h, o)
Public instance attributes: Wz, Wr, Wh, Wy, bz, br, bh, by (the weights and
    biases of the cell)
public instance method: def forward(self, h_prev, x_t)
"""
import numpy as np


class GRUCell:
    """
    Class GRUCell : represents a represents a gated recurrent unit
    """

    def __init__(self, i, h, o):
        """
        Class contructor
        Args:
            i: dimensionality of the data
            h: dimensionality of the hidden state
            o: dimensionality of the outputs
        Public instance attributes: Wz, Wr, Wh, Wy, bz, br, bh, by
            Wz and bz are for the update gate
            Wr and br are for the reset gate
            Wh and bh are for the intermediate hidden state
            Wy and by are for the output
        """
        self.Wz = np.random.randn(h + i, h)
        self.Wr = np.random.randn(h + i, h)
        self.Wh = np.random.randn(h + i, h)
        self.Wy = np.random.randn(h, o)

        self.bz = np.zeros(shape=(1, h))
        self.br = np.zeros(shape=(1, h))
        self.bh = np.zeros(shape=(1, h))
        self.by = np.zeros(shape=(1, o))

    def sigmoid(self, x):
        "sigmoid function"
        return 1 / (1 + np.exp(-x))

    def softmax(self, x):
        "softmax function"
        return np.exp(x) / np.sum(np.exp(x), axis=1, keepdims=True)

    def forward(self, h_prev, x_t):
        """
        Public instance method that performs forward propagation
            for one time step
        Args:
            x_t: numpy.ndarray of shape (m, i) that contains the data input
                for the cell
                m: batch size for the data
            h_prev: numpy.ndarray of shape (m, h) containing the previous
                hidden state
        Returns: h_next, y
            h_next: next hidden state
            y: output of the cell
        """
        h_x = np.concatenate((h_prev, x_t), axis=1)
        z_t = self.sigmoid(np.matmul(h_x, self.Wz) + self.bz)

        r_t = self.sigmoid(np.matmul(h_x, self.Wr) + self.br)

        rh_x = np.concatenate((r_t * h_prev, x_t), axis=1)
        h_t = np.tanh(np.matmul(rh_x, self.Wh) + self.bh)

        h_next = (1 - z_t) * h_prev + z_t * h_t

        y = self.softmax(np.matmul(h_next, self.Wy) + self.by)

        return h_next, y
