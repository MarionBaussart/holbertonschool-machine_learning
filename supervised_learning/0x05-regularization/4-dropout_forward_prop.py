#!/usr/bin/env python3
"""
module containing function dropout_forward_prop
"""
import numpy as np


def dropout_forward_prop(X, weights, L, keep_prob):
    """
    function that conducts forward propagation using Dropout
    Args:
        X: numpy.ndarray of shape (nx, m) containing the input data
            for the network
                nx: number of input features
                m: number of data points
        weights: dictionary of the weights and biases of the neural network
        L: number of layers in the network
        keep_prob: the probability that a node will be kept
    Return: a dictionary containing the outputs of each layer
        and the dropout mask used on each layer
    """
    cache = {}
    cache["A0"] = X

    for i in range(L):
        w = weights["W{}".format(i + 1)]
        b = weights["b{}".format(i + 1)]
        A = cache["A{}".format(i)]
        z = np.matmul(w, A) + b

        if i != (L - 1):
            A = np.tanh(z)
            dropout = np.random.binomial(
                1, keep_prob, size=(A.shape[0], A.shape[1]))
            cache["D{}".format(i + 1)] = dropout
            A = np.multiply(A, dropout) / keep_prob
        else:
            A = np.exp(z) / np.exp(z).sum(axis=0, keepdims=True)

        cache["A{}".format(i + 1)] = A

    return cache
