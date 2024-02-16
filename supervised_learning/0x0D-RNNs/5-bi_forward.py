#!/usr/bin/env python3
"""
module containing class BidirectionalCell:
Class constructor: def __init__(self, i, h, o)
Public instance attributes: Whf, Whb, Wy, bhf, bhb, by
    (the weights and biases of the cell)
public instance method: def forward(self, h_prev, x_t)
"""
import numpy as np


class BidirectionalCell:
    """
    Class BidirectionalCell : represents a bidirectional cell of an RNN
    """

    def __init__(self, i, h, o):
        """
        Class contructor
        Args:
            i: dimensionality of the data
            h: dimensionality of the hidden state
            o: dimensionality of the outputs
        Public instance attributes: Whf, Whb, Wy, bhf, bhb, by
            Whf and bhf are for the hidden states in the forward direction
            Whb and bhb are for the hidden states in the backward direction
            Wy and by are for the outputs
        """
        self.Whf = np.random.randn(h + i, h)
        self.Whb = np.random.randn(h + i, h)
        self.Wy = np.random.randn(2 * h, o)

        self.bhf = np.zeros(shape=(1, h))
        self.bhb = np.zeros(shape=(1, h))
        self.by = np.zeros(shape=(1, o))

    def forward(self, h_prev, x_t):
        """
        Public instance method that calculates the hidden state in the forward
            direction for one time step
        Args:
            x_t: numpy.ndarray of shape (m, i) that contains the data input
                for the cell
                m: batch size for the data
            h_prev: numpy.ndarray of shape (m, h) containing the previous
                hidden state
        Returns: h_next
            h_next: next hidden state

        """
        h_x = np.concatenate((h_prev, x_t), axis=1)
        h_next = np.tanh(np.matmul(h_x, self.Whf) + self.bhf)

        return h_next
