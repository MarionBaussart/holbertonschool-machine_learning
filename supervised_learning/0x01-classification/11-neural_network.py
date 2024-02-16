#!/usr/bin/env python3
"""
module containing class NeuralNetwork:
Class constructor: def __init__(self, nx, nodes)
Private instance attributes: __W1, __b1, __A1, __W2, __b2, __A2
Public method def forward_prop(self, X)
Public method def cost(self, Y, A)
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

    def forward_prop(self, X):
        """
        Public method that calculates the forward propagation of the neural
            network
        Args:
            X: numpy.ndarray with shape (nx, m) that contains the input data
            with nx: number of input features to the neuron
            and m: number of examples
        Returns the updated private attribute __A1 and __A2 with
            sigmoid activation function :
                1 / 1 + e^(-x) with x = Sum(Wi*Xi + b) for i=0 to nx
        """
        z1 = np.matmul(self.__W1, X) + self.__b1
        self.__A1 = 1 / (1 + np.exp(-z1))
        z2 = np.matmul(self.__W2, self.__A1) + self.__b2
        self.__A2 = 1 / (1 + np.exp(-z2))
        return self.__A1, self.__A2

    def cost(self, Y, A):
        """
        Public method that calculates the cost of the model
        using logistic regression
        Args:
            Y: numpy.ndarray with shape (1, m) that contains the correct labels
                for the input data with m: number of examples
            A: numpy.ndarray with shape (1, m) containing the activated output
                of the neuron for each example
        Returns the cost:
            cost = -1/m * Sum(Yi*log(Ai) + (1-Yi)*log(1-Ai))
        """
        m = Y.shape[1]
        cost = - (1 / m) * \
            (np.sum((Y * np.log(A)) + (1 - Y) * np.log(1.0000001 - A)))
        return cost
