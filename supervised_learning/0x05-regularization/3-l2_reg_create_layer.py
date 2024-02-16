#!/usr/bin/env python3
"""
module containing function l2_reg_create_layer
"""
import tensorflow.compat.v1 as tf


def l2_reg_create_layer(prev, n, activation, lambtha):
    """
    function that creates a tensorflow layer that includes L2 regularization
    Args:
        prev: the tensor output of the previous layer
        n: the number of nodes in the layer to create
        activation: the activation function that the layer should use
        lambtha: L2 regularization parameter
    Return: the tensor output of the new layer
    """
    layer_weights = tf.keras.initializers.VarianceScaling(
        scale=2.0,
        mode=("fan_avg"))

    l2 = tf.keras.regularizers.L2(lambtha)

    layer = tf.layers.Dense(
        n,
        activation=activation,
        kernel_initializer=layer_weights,
        kernel_regularizer=l2,
        name="layer"
    )

    return layer(prev)
