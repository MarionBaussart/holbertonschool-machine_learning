#!/usr/bin/env python3
"""
module containing function update_variables_momentum
"""


def update_variables_momentum(alpha, beta1, var, grad, v):
    """
    function that updates a variable using the gradient descent
        with momentum optimization algorithm
    Args:
        alpha: the learning rate
        beta1: the momentum weight
        var: a numpy.ndarray containing the variable to be updated
        grad: a numpy.ndarray containing the gradient of var
        v: the previous first moment of var
    Return: the updated variable and the new moment
    v_dW = beta*v_dW + (1-beta)*dW
    W = W - alpha*v_dW
    """
    new_moment = (beta1 * v) + (1 - beta1) * grad
    updated_variable = var - (alpha * new_moment)

    return updated_variable, new_moment
