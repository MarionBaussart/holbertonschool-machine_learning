#!/usr/bin/env python3
"""
module containing class Neuron:
Class constructor def __init__(self, nx)
Private instance attributes: __W, __b, __A
Public method def forward_prop(self, X)
Public method def cost(self, Y, A)
"""
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
        Private instance attributes:
            W: weights vector for the neuron
            b: bias for the neuron
            A: activated output of the neuron (prediction)
        """
        if type(nx) != int:
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")

        self.__W = np.random.randn(1, nx)
        self.__b = 0
        self.__A = 0

    @property
    def W(self):
        """
        getter function
        __W: weights vector for the neuron
        return private instance attribute __W
        """
        return self.__W

    @property
    def b(self):
        """
        getter function
        __b: bias for the neuron
        return private instance attribute __b
        """
        return self.__b

    @property
    def A(self):
        """
        getter function
        __A: activated output of the neuron (prediction)
        return private instance attribute __A
        """
        return self.__A

    def forward_prop(self, X):
        """
        Public method that calculates the forward propagation of the neuron
        Args:
            X: numpy.ndarray with shape (nx, m) that contains the input data
            with nx: number of input features to the neuron
            and m: number of examples
        Returns the updated private attribute __A with
        sigmoid activation function :
            1 / 1 + e^(-x) with x = Sum(Wi*Xi + b) for i=0 to nx
        """
        z = np.matmul(self.__W, X) + self.__b
        self.__A = 1 / (1 + np.exp(-z))
        return self.__A

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
