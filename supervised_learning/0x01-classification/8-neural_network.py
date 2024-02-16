#!/usr/bin/env python3
"""
module containing class NeuralNetwork:
Class constructor: def __init__(self, nx, nodes)
"""
import numpy as np


class NeuralNetwork:
    """
    Class NeuralNetwork : defines a neural network with one hidden layer
        performing binary classification
    """

    def __init__(self, nx, nodes):
        """
        Class contructor
        Args:
            nx: the number of input features to the neuron
            nodes: the number of nodes found in the hidden layer
        Public instance attributes:
            W1: weights vector for the hidden layer
            b1: bias for the hidden layer
            A1: activated output of the hidden layer
            W2: weights vector for the output neuron
            b2: bias for the output neuron
            A2: activated output of the output neuron
        """
        if type(nx) != int:
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        if type(nodes) != int:
            raise TypeError("nodes must be an integer")
        if nodes < 1:
            raise ValueError("nodes must be a positive integer")

        self.W1 = np.random.randn(nodes, nx)
        self.b1 = np.zeros([nodes, 1])
        self.A1 = 0
        self.W2 = np.random.randn(1, nodes)
        self.b2 = 0
        self.A2 = 0
