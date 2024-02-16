#!/usr/bin/env python3
"""
module containing function create_momentum_op
"""
import tensorflow.compat.v1 as tf


def create_momentum_op(loss, alpha, beta1):
    """
    function that creates the training operation for a neural network
        in tensorflow using the gradient descent
        with momentum optimization algorithm
    Args:
        loss: the loss of the network
        alpha: the learning rate
        beta1: the momentum weight
    Return: the momentum optimization operation
    """
    optimizer = tf.train.MomentumOptimizer(learning_rate=alpha,
                                           momentum=beta1,
                                           name='momentum')
    momentum = optimizer.minimize(loss)
    return momentum
