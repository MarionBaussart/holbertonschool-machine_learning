#!/usr/bin/env python3
"""
module containing function update_variables_RMSProp
"""
import numpy as np


def update_variables_RMSProp(alpha, beta2, epsilon, var, grad, s):
    """
    function that updates a variable using the RMSProp optimization algorithm
    Args:
        alpha: the learning rate
        beta2: the RMSProp weight
        epsilon: a small number to avoid division by zero
        var: a numpy.ndarray containing the variable to be updated
        grad: a numpy.ndarray containing the gradient of var
        s: the previous second moment of var
    Return: the updated variable and the new moment
    v_dW = beta*v_dW + (1-beta)*dW²
    W = W - alpha * (dW / (sqrt(v_dW) + epsilon))
    """
    new_moment = (beta2 * s) + (1 - beta2) * grad * grad
    updated_variable = var - (alpha * (grad / (np.sqrt(new_moment) + epsilon)))

    return updated_variable, new_moment
