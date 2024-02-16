#!/usr/bin/env python3
"""
module containing function create_batch_norm_layer
"""
import tensorflow.compat.v1 as tf


def create_batch_norm_layer(prev, n, activation):
    """
    function that creates a batch normalization layer
        for a neural network in tensorflow
    Args:
        prev: the activated output of the previous layer
        n: the number of nodes in the layer to be created
        activation: the activation function that should be
            used on the output of the layer
    Return: a tensor of the activated output for the layer
    """
    layer_weights = tf.keras.initializers.VarianceScaling(mode='fan_avg')

    layer = tf.layers.Dense(
        n,
        activation=None,
        kernel_initializer=layer_weights,
        name="layer"
    )

    batch_mean, batch_variance = tf.nn.moments(layer(prev), [0])
    beta = tf.Variable(tf.zeros(shape=[n]))
    gamma = tf.Variable(tf.ones(shape=[n]))
    epsilon = 1e-8

    batch_norm = tf.nn.batch_normalization(
        x=layer(prev),
        mean=batch_mean,
        variance=batch_variance,
        offset=beta,
        scale=gamma,
        variance_epsilon=epsilon)

    return activation(batch_norm)
