#!/usr/bin/env python3
"""
module containing class DeepNeuralNetwork
"""
import numpy as np


class DeepNeuralNetwork:
    """
    Class DeepNeuralNetwork : defines a deep neural network
        performing binary classification
    Class constructor: def __init__(self, nx, layers)
    Public method: def forward_prop(self, X)
    """

    def __init__(self, nx, layers):
        """
        Class contructor
        Args:
            nx: the number of input features to the neural network
            layers: a list representing the number of nodes in each layer
                of the network
        Private instance attributes:
            L: the number of layers in the neural network
            cache: a dictionary to hold all intermediary values of the network
            weights: a dictionary to hold all weights and biased of the network
        """
        if type(nx) != int:
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        if type(layers) != list or layers == []:
            raise TypeError("layers must be a list of positive integers")

        self.__L = len(layers)
        self.__cache = {}
        self.__weights = {}

        for i in range(len(layers)):
            if type(layers[i]) != int or layers[i] < 0:
                raise TypeError("layers must be a list of positive integers")
            b = np.zeros((layers[i], 1))
            w = np.random.randn(layers[i], nx) * \
                np.sqrt(2 / nx)
            self.__weights["b{}".format(i + 1)] = b
            self.__weights["W{}".format(i + 1)] = w
            nx = layers[i]

    @property
    def L(self):
        """
        getter function
        __L: the number of layers in the neural network
        return private instance attribute __L
        """
        return self.__L

    @property
    def cache(self):
        """
        getter function
        __cache: a dictionary to hold all intermediary values of the network
        return private instance attribute __cache
        """
        return self.__cache

    @property
    def weights(self):
        """
        getter function
        __weights: a dictionary to hold all weights and biased of the network
        return private instance attribute __weights
        """
        return self.__weights

    def forward_prop(self, X):
        """
        Public method that calculates the forward propagation of the neural
            network
        Args:
            X: numpy.ndarray with shape (nx, m) that contains the input data
            with nx: number of input features to the neuron
            and m: number of examples
        Returns the output of the neural network and the cache
        """
        self.__cache["A0"] = X
        for i in range(self.__L):
            w = self.__weights["W{}".format(i + 1)]
            cache = self.__cache["A{}".format(i)]
            b = self.__weights["b{}".format(i + 1)]
            z = np.matmul(w, cache) + b
            A = 1 / (1 + np.exp(-z))
            self.__cache["A{}".format(i + 1)] = A
        return A, self.__cache
