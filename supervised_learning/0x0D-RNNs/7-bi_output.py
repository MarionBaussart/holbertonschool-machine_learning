#!/usr/bin/env python3
"""
module containing class BidirectionalCell:
Class constructor: def __init__(self, i, h, o)
Public instance attributes: Whf, Whb, Wy, bhf, bhb, by
    (the weights and biases of the cell)
public instance method:
    def forward(self, h_prev, x_t)
    def backward(self, h_next, x_t)
    def output(self, H)
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

    def backward(self, h_next, x_t):
        """
        Public instance method that calculates the hidden state in the backward
            direction for one time step
        Args:
            x_t: numpy.ndarray of shape (m, i) that contains the data input
                for the cell
                m: batch size for the data
            h_prev: numpy.ndarray of shape (m, h) containing the next hidden
                state
        Returns: h_prev
            h_prev: previous hidden state

        """
        h_x = np.concatenate((h_next, x_t), axis=1)
        h_prev = np.tanh(np.matmul(h_x, self.Whb) + self.bhb)

        return h_prev

    def softmax(self, x):
        "softmax function"
        return np.exp(x) / np.sum(np.exp(x), axis=1, keepdims=True)

    def output(self, H):
        """
        Public instance method that calculates all outputs for the RNN
        Args:
            H: numpy.ndarray of shape (t, m, 2 * h)
                contains the concatenated hidden states from both directions,
                excluding their initialized states
                t: number of time steps
                m: batch size for the data
                h: dimensionality of the hidden states
        Returns: Y, the outputs
        """
        t = H.shape[0]
        m = H.shape[1]
        o = self.by.shape[1]

        Y = np.zeros(shape=(t, m, o))

        for time_step in range(t):
            z = np.matmul(H[time_step], self.Wy) + self.by
            Y[time_step] = self.softmax(z)

        return Y
