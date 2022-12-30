#!/usr/bin/env python3
import numpy as np
"""module containing class Neuron"""


class Neuron:
    """
    Class Neuron : defines a single neuron performing binary classification
    """

    def __init__(self, nx):
        """
        Class contructor
        Args:
            nx: the number of input features to the neuron
        Public instance attributes:
            W: weights vector for the neuron
            b: bias for the neuron
            A: activated output of the neuron (prediction)
        """
        if type(nx) != int:
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")

        self.W = np.expand_dims(np.random.randn(nx), axis=0)
        self.b = 0
        self.A = 0
