#!/usr/bin/env python3
"""
module containing function create_RMSProp_op
"""
import tensorflow.compat.v1 as tf


def create_RMSProp_op(loss, alpha, beta2, epsilon):
    """
    function that creates the training operation for a neural network
        in tensorflow using the RMSProp optimization algorithm
    Args:
        loss: the loss of the network
        alpha: the learning rate
        beta2: the RMSProp weight
        epsilon: a small number to avoid division by zero
    Return: the RMSProp optimization operation
    """
    optimizer = tf.train.RMSPropOptimizer(learning_rate=alpha,
                                          decay=beta2,
                                          epsilon=epsilon,
                                          name='RMSProp')
    rms_prop_op = optimizer.minimize(loss)
    return rms_prop_op
