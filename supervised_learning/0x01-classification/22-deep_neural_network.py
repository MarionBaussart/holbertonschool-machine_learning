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
    Public method: def cost(self, Y, A)
    Public method: def evaluate(self, X, Y)
    Public method: def gradient_descent(self, Y, cache, alpha=0.05)
    Public method: def train(self, X, Y, iterations=5000, alpha=0.05)
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

    def evaluate(self, X, Y):
        """
        Public method that evaluates the neural network's predictions
        Args:
            X: numpy.ndarray with shape (nx, m) that contains the input data
                with nx: number of input features to the neuron
                and m: number of examples
            Y: numpy.ndarray with shape (1, m) that contains the correct labels
                for the input data
        Returns the neuron's prediction and the cost of the network
        """
        self.__A, self.__cache = self.forward_prop(X)
        cost = self.cost(Y, self.__A)
        activated_output = np.where(self.__A >= 0.5, 1, 0)
        return activated_output, cost

    def gradient_descent(self, Y, cache, alpha=0.05):
        """
        Public method that calculates one pass of gradient descent
        on the deep neural network
        Updates the private attribute __weights
        Args:
            Y: numpy.ndarray with shape (1, m) that contains the correct labels
                for the input data
            cache: a dictionary containing all the intermediary values
                of the network
            alpha: the learning rate
        """
        m = Y.shape[1]
        dz = cache["A{}".format(self.__L)] - Y

        for i in range(self.__L, 0, -1):
            A = cache["A{}".format(i - 1)]
            dw = (1 / m) * np.matmul(dz, A.T)
            db = (1 / m) * np.sum(dz, axis=1, keepdims=True)
            dz = np.matmul(self.__weights["W{}".format(i)].T, dz) * \
                (A * (1 - A))

            self.__weights["W{}".format(i)] = self.__weights["W{}".format(i)] \
                - (alpha * dw)
            self.__weights["b{}".format(i)] = self.__weights["b{}".format(i)] \
                - (alpha * db)

    def train(self, X, Y, iterations=5000, alpha=0.05):
        """
        Public method that trains the deep neural network
        Updates the private attributes __weights and __cache
        Args:
            X: numpy.ndarray with shape (nx, m) that contains the input data
                with nx: number of input features to the neuron
                and m: number of examples
            Y: numpy.ndarray with shape (1, m) that contains the correct labels
                for the input data
            iterations: the number of iterations to train over
            alpha: the learning rate
        """
        if type(iterations) != int:
            raise TypeError("iterations must be an integer")
        if iterations < 0:
            raise ValueError("iterations must be a positive integer")
        if type(alpha) != float:
            raise TypeError("alpha must be a float")
        if alpha < 0:
            raise ValueError("alpha must be positive")

        for i in range(iterations):
            self.__A, self.__cache = self.forward_prop(X)
            self.gradient_descent(Y, self.__cache, alpha)

        return self.evaluate(X, Y)
