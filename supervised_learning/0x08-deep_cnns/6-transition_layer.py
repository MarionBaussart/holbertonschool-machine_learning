#!/usr/bin/env python3
"""
module containing function transition_layer
"""
import tensorflow.keras as K


def transition_layer(X, nb_filters, compression):
    """
    function that builds a transition layer as described in
        Densely Connected Convolutional Networks
    Args: X: output from the previous layer
        nb_filters: integer representing the number of filters in X
        compression: compression factor for the transition layer
    Return: output of the transition layer
        and the number of filters within the output
    """
    initializer_kernel_weights = K.initializers.HeNormal(seed=None)

    batch_normalization = K.layers.BatchNormalization(axis=3)(X)
    activated_output = K.layers.Activation('relu')(batch_normalization)
    conv_1x1 = K.layers.Conv2D(
            filters=nb_filters * compression,
            kernel_size=(1, 1),
            padding='same',
            kernel_initializer=initializer_kernel_weights
        )(activated_output)
    average_pooling = K.layers.AveragePooling2D(
        pool_size=(2, 2),
        strides=(2, 2),
        padding='same'
    )(conv_1x1)

    nb_filters = int(nb_filters * compression)

    return average_pooling, nb_filters
