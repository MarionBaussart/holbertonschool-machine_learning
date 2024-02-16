#!/usr/bin/env python3
"""
module containing function inception_block
"""
import tensorflow.keras as K


def inception_block(A_prev, filters):
    """
    function that builds an inception block
    Args:
        A_prev: output from the previous layer
        filters: tuple or list containing F1, F3R, F3,F5R, F5, FPP
            F1: number of filters in the 1x1 convolution
            F3R: number of filters in the 1x1 convolution
                before the 3x3 convolution
            F3: number of filters in the 3x3 convolution
            F5R: number of filters in the 1x1 convolution
                before the 5x5 convolution
            F5: number of filters in the 5x5 convolution
            FPP: number of filters in the 1x1 convolution
                after the max pooling
    Return: concatenated output of the inception block
    """
    F1 = filters[0]
    F3R = filters[1]
    F3 = filters[2]
    F5R = filters[3]
    F5 = filters[4]
    FPP = filters[5]

    initializer_kernel_weights = K.initializers.HeNormal(seed=None)

    # Convolutional layer with F1 kernels of shape 1x1 with same padding
    layer_F1 = K.layers.Conv2D(
        filters=F1,
        kernel_size=(1, 1),
        padding='same',
        activation='relu',
        kernel_initializer=initializer_kernel_weights
    )(A_prev)

    # Convolutional layer with F3R kernels of shape 1x1 with same padding
    layer_F3R = K.layers.Conv2D(
        filters=F3R,
        kernel_size=(1, 1),
        padding='same',
        activation='relu',
        kernel_initializer=initializer_kernel_weights
    )(A_prev)

    # Convolutional layer with F3 kernels of shape 3x3 with same padding
    layer_F3 = K.layers.Conv2D(
        filters=F3,
        kernel_size=(3, 3),
        padding='same',
        activation='relu',
        kernel_initializer=initializer_kernel_weights
    )(layer_F3R)

    # Convolutional layer with F5R kernels of shape 1x1 with same padding
    layer_F5R = K.layers.Conv2D(
        filters=F5R,
        kernel_size=(1, 1),
        padding='same',
        activation='relu',
        kernel_initializer=initializer_kernel_weights
    )(A_prev)

    # Convolutional layer with F5 kernels of shape 5x5 with same padding
    layer_F5 = K.layers.Conv2D(
        filters=F5,
        kernel_size=(5, 5),
        padding='same',
        activation='relu',
        kernel_initializer=initializer_kernel_weights
    )(layer_F5R)

    # Max pooling layer with kernels of shape 3x3 with 1x1 strides
    layer_max_pooling = K.layers.MaxPooling2D(
        pool_size=(3, 3),
        strides=(1, 1),
        padding='same'
    )(A_prev)

    # Convolutional layer with FPP kernels of shape 1x1 with same padding
    layer_FPP = K.layers.Conv2D(
        filters=FPP,
        kernel_size=(1, 1),
        padding='same',
        activation='relu',
        kernel_initializer=initializer_kernel_weights
    )(layer_max_pooling)

    # concatenate
    output = K.layers.concatenate([layer_F1, layer_F3, layer_F5, layer_FPP])

    return output
