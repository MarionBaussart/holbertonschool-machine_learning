#!/usr/bin/env python3
"""
module containing function dense_block
"""
import tensorflow.keras as K


def dense_block(X, nb_filters, growth_rate, layers):
    """
    function that builds a dense block as described in
        Densely Connected Convolutional Networks
    Args: X: output from the previous layer
        nb_filters: integer representing the number of filters in X
        growth_rate: growth rate for the dense block
        layers: number of layers in the dense block
    Return: concatenated output of each layer within the Dense Block
        and the number of filters within the concatenated outputs
    """
    initializer_kernel_weights = K.initializers.HeNormal(seed=None)

    for layer in range(layers):
        batch_normalization = K.layers.BatchNormalization(axis=3)(X)
        activated_output = K.layers.Activation('relu')(batch_normalization)
        conv_1x1 = K.layers.Conv2D(
            filters=growth_rate * 4,
            kernel_size=(1, 1),
            padding='same',
            kernel_initializer=initializer_kernel_weights
        )(activated_output)
        batch_normalization = K.layers.BatchNormalization(axis=3)(conv_1x1)
        activated_output = K.layers.Activation('relu')(batch_normalization)
        conv_3x3 = K.layers.Conv2D(
            filters=growth_rate,
            kernel_size=(3, 3),
            padding='same',
            kernel_initializer=initializer_kernel_weights
        )(activated_output)

        X = K.layers.concatenate([X, conv_3x3])
        nb_filters += growth_rate

    return X, nb_filters
