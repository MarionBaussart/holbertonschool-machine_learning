#!/usr/bin/env python3
"""
module containing function dropout_create_layer
"""
import tensorflow.compat.v1 as tf


def dropout_create_layer(prev, n, activation, keep_prob):
    """
    function that creates a layer of a neural network using dropout
    Args:
        prev: the tensor output of the previous layer
        n: the number of nodes the new layer should contain
        activation: the activation function that the layer should use
        keep_prob: probability that a node will be kept
    Return: the tensor output of the new layer
    """
    layer_weights = tf.keras.initializers.VarianceScaling(
        scale=2.0,
        mode=("fan_avg"))

    dropout = tf.keras.layers.Dropout(keep_prob)

    layer = tf.layers.Dense(
        n,
        activation=activation,
        kernel_initializer=layer_weights,
        kernel_regularizer=dropout,
        name="layer"
    )

    return layer(prev)
