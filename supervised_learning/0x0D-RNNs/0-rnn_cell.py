#!/usr/bin/env python3
"""
module containing class RNNCell:
Class constructor: def __init__(self, i, h, o)
Public instance attributes: Wh, Wy, bh, by (the weights and biases of the cell)
public instance method: def forward(self, h_prev, x_t)
"""
import numpy as np


class RNNCell:
    """
    Class RNNCell : represents a cell of a simple RNN
    """

    def __init__(self, i, h, o):
        """
        Class contructor
        Args:
            i: dimensionality of the data
            h: dimensionality of the hidden state
            o: dimensionality of the outputs
        Public instance attributes:
            Wh, Wy, bh, by: the weights and biases of the cell
        """
        self.Wh = np.random.randn(h + i, h)
        self.Wy = np.random.randn(h, o)
        self.bh = np.zeros(shape=(1, h))
        self.by = np.zeros(shape=(1, o))

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
        h_next = np.tanh(np.matmul(h_x, self.Wh) + self.bh)

        z = np.matmul(h_next, self.Wy) + self.by
        y = np.exp(z) / np.sum(np.exp(z), axis=1, keepdims=True)

        return h_next, y
