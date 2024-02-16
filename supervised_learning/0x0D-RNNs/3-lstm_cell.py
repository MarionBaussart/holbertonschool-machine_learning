#!/usr/bin/env python3
"""
module containing class LSTMCell:
Class constructor: def __init__(self, i, h, o)
Public instance attributes: Wf, Wu, Wc, Wo, Wy, bf, bu, bc, bo, by
    (the weights and biases of the cell)
public instance method: def forward(self, h_prev, c_prev, x_t)
"""
import numpy as np


class LSTMCell:
    """
    Class LSTMCell : represents an LSTM unit
    """

    def __init__(self, i, h, o):
        """
        Class contructor
        Args:
            i: dimensionality of the data
            h: dimensionality of the hidden state
            o: dimensionality of the outputs
        Public instance attributes: Wf, Wu, Wc, Wo, Wy, bf, bu, bc, bo, by
            Wf and bf are for the forget gate
            Wu and bu are for the update gate
            Wc and bc are for the intermediate cell state
            Wo and bo are for the output gate
            Wy and by are for the outputs
        """
        self.Wf = np.random.randn(h + i, h)
        self.Wu = np.random.randn(h + i, h)
        self.Wc = np.random.randn(h + i, h)
        self.Wo = np.random.randn(h + i, h)
        self.Wy = np.random.randn(h, o)

        self.bf = np.zeros(shape=(1, h))
        self.bu = np.zeros(shape=(1, h))
        self.bc = np.zeros(shape=(1, h))
        self.bo = np.zeros(shape=(1, h))
        self.by = np.zeros(shape=(1, o))

    def sigmoid(self, x):
        "sigmoid function"
        return 1 / (1 + np.exp(-x))

    def softmax(self, x):
        "softmax function"
        return np.exp(x) / np.sum(np.exp(x), axis=1, keepdims=True)

    def forward(self, h_prev, c_prev, x_t):
        """
        Public instance method that performs forward propagation
            for one time step
        Args:
            x_t: numpy.ndarray of shape (m, i) that contains the data input
                for the cell
                m: batch size for the data
            h_prev: numpy.ndarray of shape (m, h) containing the previous
                hidden state
            c_prev: numpy.ndarray of shape (m, h) containing the previous
                cell state
        Returns: h_next, c_next, y
            h_next: next hidden state
            c_next: next cell state
            y: output of the cell
        """
        h_x = np.concatenate((h_prev, x_t), axis=1)
        i_t = self.sigmoid(np.matmul(h_x, self.Wu) + self.bu)

        f_t = self.sigmoid(np.matmul(h_x, self.Wf) + self.bf)

        o_t = self.sigmoid(np.matmul(h_x, self.Wo) + self.bo)

        candidate_t = np.tanh(np.matmul(h_x, self.Wc) + self.bc)

        c_next = f_t * c_prev + i_t * candidate_t

        h_next = o_t * np.tanh(c_next)

        y = self.softmax(np.matmul(h_next, self.Wy) + self.by)

        return h_next, c_next, y
