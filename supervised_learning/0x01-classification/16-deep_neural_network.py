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
    """

    def __init__(self, nx, layers):
        """
        Class contructor
        Args:
            nx: the number of input features to the neural network
            layers: a list representing the number of nodes in each layer
                of the network
        Public instance attributes:
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

        self.L = len(layers)
        self.cache = {}
        self.weights = {}

        for i in range(len(layers)):
            if type(layers[i]) != int or layers[i] < 0:
                raise TypeError("layers must be a list of positive integers")
            b = np.zeros((layers[i], 1))
            w = np.random.randn(layers[i], nx) * \
                np.sqrt(2 / nx)
            self.weights["b{}".format(i + 1)] = b
            self.weights["W{}".format(i + 1)] = w
            nx = layers[i]
