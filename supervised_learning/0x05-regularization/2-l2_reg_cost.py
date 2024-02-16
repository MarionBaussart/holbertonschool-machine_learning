#!/usr/bin/env python3
"""
module containing function l2_reg_cost
"""
import tensorflow.compat.v1 as tf


def l2_reg_cost(cost):
    """
    function that calculates the cost of a neural network
        with L2 regularization
    Args:
        cost: tensor containing the cost of the network
            without L2 regularization
    Return: a tensor containing the cost of the network
        accounting for L2 regularization
    """
    l2_cost = tf.losses.get_regularization_losses()

    return cost + l2_cost
