#!/usr/bin/env python3
"""module containing class Neuron"""
import numpy as np


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

        # np.expand_dims: add a dimension to the matrix
        self.W = np.random.randn(1, nx)
        self.b = 0
        self.A = 0
