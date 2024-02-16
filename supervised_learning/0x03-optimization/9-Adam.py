#!/usr/bin/env python3
"""
module containing function update_variables_Adam
"""
import numpy as np


def update_variables_Adam(alpha, beta1, beta2, epsilon, var, grad, v, s, t):
    """
    function that updates a variable in place
        using the Adam optimization algorithm
    Args:
        alpha: the learning rate
        beta1: the weight used for the first moment
        beta2: the weight used for the second moment
        epsilon: a small number to avoid division by zero
        var: a numpy.ndarray containing the variable to be updated
        grad: a numpy.ndarray containing the gradient of var
        v: the previous first moment of var
        s: the previous second moment of var
        t: the time step used for bias correction
    Return: the updated variable,
        the new first moment,
        and the new second moment
    Update first moment:
        v_dW = beta1*v_dW + (1-beta1)*dW
    Update second moment:
        s_dW = beta2*s_dW + (1-beta2)*dW²
    bias correction:
        v_dW_corrected = v_dW / (1-beta1**t)
        s_dW_corrected = s_dW / (1-beta2**t)
    update variable:
        W = W - alpha*(v_dW_corrected/(sqrt(s_dW_corrected) + epsilon))
    """
    first_moment = (beta1 * v) + ((1 - beta1) * grad)
    second_moment = (beta2 * s) + ((1 - beta2) * (grad ** 2))
    first_moment_corrected = first_moment / (1 - (beta1 ** t))
    second_moment_corrected = second_moment / (1 - (beta2 ** t))
    updated_variable = var - (alpha * (first_moment_corrected /
                                       (np.sqrt(second_moment_corrected) +
                                        epsilon)))

    return updated_variable, first_moment, second_moment
