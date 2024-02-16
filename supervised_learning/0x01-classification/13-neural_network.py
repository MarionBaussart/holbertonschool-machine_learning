#!/usr/bin/env python3
"""
module containing class NeuralNetwork:
Class constructor: def __init__(self, nx, nodes)
Private instance attributes: __W1, __b1, __A1, __W2, __b2, __A2
Public method: def forward_prop(self, X)
Public method: def cost(self, Y, A)
Public method: def evaluate(self, X, Y)
Public method def gradient_descent(self, X, Y, A1, A2, alpha=0.05)
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

    def evaluate(self, X, Y):
        """
        Public method that evaluates the neuron's predictions
        Args:
            X: numpy.ndarray with shape (nx, m) that contains the input data
                with nx: number of input features to the neuron
                and m: number of examples
            Y: numpy.ndarray with shape (1, m) that contains the correct labels
                for the input data
        Returns the neuron's prediction: numpy.ndarray with shape (1, m)
            containing the predicted labels for each example
            and the cost of the network
        """
        self.__A1, self.__A2 = self.forward_prop(X)
        cost = self.cost(Y, self.__A2)
        activated_output = np.where(self.__A2 >= 0.5, 1, 0)
        return activated_output, cost

    def gradient_descent(self, X, Y, A1, A2, alpha=0.05):
        """
        Public method that calculates one pass of gradient descent
        on the neuron
        Updates the private attributes __W1, __b1, __W2 and __b2
        Args:
            X: numpy.ndarray with shape (nx, m) that contains the input data
                with nx: number of input features to the neuron
                and m: number of examples
            Y: numpy.ndarray with shape (1, m) that contains the correct labels
                for the input data
            A1: the output of the hidden layer
                numpy.ndarray with shape (1, m) containing the activated output
                of the neuron for each example
            A2: the predicted output
                numpy.ndarray with shape (1, m) containing the activated output
                of the neuron for each example
            alpha: the learning rate
        """
        m = Y.shape[1]
        dz2 = A2 - Y
        dw2 = (1 / m) * np.matmul(dz2, A1.T)
        db2 = (1 / m) * np.sum(dz2)
        dz1 = np.matmul(self.__W2.T, dz2) * (A1 * (1 - A1))
        dw1 = (1 / m) * np.matmul(dz1, X.T)
        db1 = (1 / m) * np.sum(dz1)

        self.__W1 = self.__W1 - (alpha * dw1)
        self.__b1 = self.__b1 - (alpha * db1)
        self.__W2 = self.__W2 - (alpha * dw2)
        self.__b2 = self.__b2 - (alpha * db2)
