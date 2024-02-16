#!/usr/bin/env python3
"""
module containing class NeuralNetwork:
Class constructor: def __init__(self, nx, nodes)
Private instance attributes: __W1, __b1, __A1, __W2, __b2, __A2
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
        Private instance attributes:
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

        self.__W1 = np.random.randn(nodes, nx)
        self.__b1 = np.zeros([nodes, 1])
        self.__A1 = 0
        self.__W2 = np.random.randn(1, nodes)
        self.__b2 = 0
        self.__A2 = 0

    @property
    def W1(self):
        """
        getter function
        __W1: weights vector for the hidden layer
        return private instance attribute __W1
        """
        return self.__W1

    @property
    def b1(self):
        """
        getter function
        __b1: bias for the hidden layer
        return private instance attribute __b1
        """
        return self.__b1

    @property
    def A1(self):
        """
        getter function
        __A1: activated output of the hidden layer
        return private instance attribute __A1
        """
        return self.__A1

    @property
    def W2(self):
        """
        getter function
        __W2: weights vector for the output neuron
        return private instance attribute __W2
        """
        return self.__W2

    @property
    def b2(self):
        """
        getter function
        __b2: bias for the output neuron
        return private instance attribute __b2
        """
        return self.__b2

    @property
    def A2(self):
        """
        getter function
        __A2: activated output of the output neuron
        return private instance attribute __A2
        """
        return self.__A2
