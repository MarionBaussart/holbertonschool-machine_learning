#!/usr/bin/env python3
"""
module containing function l2_reg_cost
"""
import numpy as np


def l2_reg_cost(cost, lambtha, weights, L, m):
    """
    function that calculates the cost of a neural network
        with L2 regularization
    Args:
        cost: cost of the network without L2 regularization
        lambtha: regularization parameter
        weights: dictionary of the weights and biases (numpy.ndarrays)
            of the neural network
        L: number of layers in the neural network
        m: number of data points used
    Return: cost of the network accounting for L2 regularization
    L2_cost = cost + lambda/2m * sum(weight²)
    """
    sum_weight = 0
    for i in range(1, L + 1):
        weight = weights["W{}".format(i)]
        sum_weight += np.sum(weight ** 2)

    l2_cost = cost + (lambtha / (2 * m)) * sum_weight

    return l2_cost
