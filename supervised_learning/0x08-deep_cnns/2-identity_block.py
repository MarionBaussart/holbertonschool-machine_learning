#!/usr/bin/env python3
"""
module containing function identity_block
"""
import tensorflow.keras as K


def identity_block(A_prev, filters):
    """
    function that builds the inception network
    Args:
        A_prev: output from the previous layer
        filters: tuple or list containing F11, F3, F12, respectively:
            F11: number of filters in the first 1x1 convolution
            F3: number of filters in the 3x3 convolution
            F12: number of filters in the second 1x1 convolution
    Return: the activated output of the identity block
    """
    F11 = filters[0]
    F3 = filters[1]
    F12 = filters[2]

    initializer_kernel_weights = K.initializers.HeNormal(seed=None)

    output_layer = K.layers.Conv2D(
        filters=F11,
        kernel_size=(1, 1),
        strides=(1, 1),
        padding='same',
        kernel_initializer=initializer_kernel_weights
    )(A_prev)
    batch_normalization = K.layers.BatchNormalization(axis=3)(output_layer)
    activated_output = K.layers.Activation('relu')(batch_normalization)

    output_layer = K.layers.Conv2D(
        filters=F3,
        kernel_size=(3, 3),
        padding='same',
        kernel_initializer=initializer_kernel_weights
    )(activated_output)
    batch_normalization = K.layers.BatchNormalization(axis=3)(output_layer)
    activated_output = K.layers.Activation('relu')(batch_normalization)

    output_layer = K.layers.Conv2D(
        filters=F12,
        kernel_size=(1, 1),
        padding='same',
        kernel_initializer=initializer_kernel_weights
    )(activated_output)
    batch_normalization = K.layers.BatchNormalization(axis=3)(output_layer)
    add = K.layers.Add()([batch_normalization, A_prev])
    activated_output = K.layers.Activation('relu')(add)

    return activated_output
