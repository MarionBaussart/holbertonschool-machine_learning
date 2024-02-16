#!/usr/bin/env python3
"""
module containing function create_Adam_op
"""
import tensorflow.compat.v1 as tf


def create_Adam_op(loss, alpha, beta1, beta2, epsilon):
    """
    function that creates the training operation for a neural network
        in tensorflow using the Adam optimization algorithm
    Args:
        loss: the loss of the network
        alpha: the learning rate
        beta1: the weight used for the first moment
        beta2: the weight used for the second moment
        epsilon: a small number to avoid division by zero
    Return: the Adam optimization operation
    """
    optimizer = tf.train.AdamOptimizer(learning_rate=alpha,
                                       beta1=beta1,
                                       beta2=beta2,
                                       epsilon=epsilon,
                                       name='Adam')
    adam_op = optimizer.minimize(loss)
    return adam_op
