#!/usr/bin/env python3
"""
module containing function l2_reg_gradient_descent
"""
import numpy as np


def l2_reg_gradient_descent(Y, weights, cache, alpha, lambtha, L):
    """
    function that updates the weights and biases of a neural network
        using gradient descent with L2 regularization
    Args:
        Y: one-hot numpy.ndarray of shape (classes, m)
            that contains the correct labels for the data
                classes: number of classes
                m: number of data points
        weights: dictionary of the weights and biases of the neural network
        cache: dictionary of the outputs of each layer of the neural network
        alpha: learning rate
        lambtha: L2 regularization parameter
        L: number of layers of the network
    Return: no return
    """
    m = Y.shape[1]
    dz = cache["A{}".format(L)] - Y
    for i in range(L, 0, -1):
        w = weights["W{}".format(i)]
        b = weights["b{}".format(i)]
        A_0 = cache["A{}".format(i - 1)]

        dw = (1 / m) * (np.matmul(dz, A_0.T) + (lambtha * w))
        db = (1 / m) * np.sum(dz, axis=1, keepdims=True)
        dz = np.matmul(w.T, dz) * (1 - (A_0 ** 2))

        weights["W{}".format(i)] = w - (alpha * dw)
        weights["b{}".format(i)] = b - (alpha * db)
