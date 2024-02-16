#!/usr/bin/env python3
"""
module containing function inception_network
"""
import tensorflow.keras as K
inception_block = __import__('0-inception_block').inception_block


def inception_network():
    """
    function that builds the inception network
    Return: the keras model
    """
    inputs = K.Input(shape=(224, 224, 3))

    # create layers
    output = K.layers.Conv2D(
        filters=64,
        kernel_size=(7, 7),
        strides=(2, 2),
        padding='same',
        activation='relu'
    )(inputs)

    output = K.layers.MaxPooling2D(
        pool_size=(3, 3),
        strides=(2, 2),
        padding='same'
    )(output)

    output = K.layers.Conv2D(
        filters=64,
        kernel_size=(1, 1),
        strides=(1, 1),
        padding='same',
        activation='relu'
    )(output)

    output = K.layers.Conv2D(
        filters=192,
        kernel_size=(3, 3),
        strides=(1, 1),
        padding='same',
        activation='relu'
    )(output)

    output = K.layers.MaxPooling2D(
        pool_size=(3, 3),
        strides=(2, 2),
        padding='same'
    )(output)

    output = inception_block(output, [64, 96, 128, 16, 32, 32])
    output = inception_block(output, [128, 128, 192, 32, 96, 64])

    output = K.layers.MaxPooling2D(
        pool_size=(3, 3),
        strides=(2, 2),
        padding='same'
    )(output)

    output = inception_block(output, [192, 96, 208, 16, 48, 64])
    output = inception_block(output, [160, 112, 224, 24, 64, 64])
    output = inception_block(output, [128, 128, 256, 24, 64, 64])
    output = inception_block(output, [112, 144, 288, 32, 64, 64])
    output = inception_block(output, [256, 160, 320, 32, 128, 128])

    output = K.layers.MaxPooling2D(
        pool_size=(3, 3),
        strides=(2, 2),
        padding='same'
    )(output)

    output = inception_block(output, [256, 160, 320, 32, 128, 128])
    output = inception_block(output, [384, 192, 384, 48, 128, 128])

    output = K.layers.AveragePooling2D(
        pool_size=(7, 7),
        strides=(1, 1)
    )(output)

    output = K.layers.Dropout(
        rate=0.4
    )(output)

    output = K.layers.Dense(
        units=1000,
        activation='softmax'
    )(output)

    model = K.Model(inputs=inputs, outputs=output)

    return model
