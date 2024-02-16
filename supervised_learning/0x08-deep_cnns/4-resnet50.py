#!/usr/bin/env python3
"""
module containing function resnet50
"""
import tensorflow.keras as K
identity_block = __import__('2-identity_block').identity_block
projection_block = __import__('3-projection_block').projection_block


def resnet50():
    """
    function that builds the ResNet-50 architecture
        as described in Deep Residual Learning for Image Recognition (2015)
    Return: the keras model
    """
    inputs = K.Input(shape=(224, 224, 3))

    initializer_kernel_weights = K.initializers.HeNormal(seed=None)

    output_layer = K.layers.Conv2D(
        filters=64,
        kernel_size=(7, 7),
        strides=(2, 2),
        padding='same',
        kernel_initializer=initializer_kernel_weights
    )(inputs)
    batch_normalization = K.layers.BatchNormalization(axis=3)(output_layer)
    activated_output = K.layers.Activation('relu')(batch_normalization)
    output_layer = K.layers.MaxPooling2D(
        pool_size=(3, 3),
        strides=(2, 2),
        padding='same'
    )(activated_output)

    activated_output = projection_block(output_layer, [64, 64, 256], s=1)
    activated_output = identity_block(activated_output, [64, 64, 256])
    activated_output = identity_block(activated_output, [64, 64, 256])

    activated_output = projection_block(activated_output, [128, 128, 512])
    activated_output = identity_block(activated_output, [128, 128, 512])
    activated_output = identity_block(activated_output, [128, 128, 512])
    activated_output = identity_block(activated_output, [128, 128, 512])

    activated_output = projection_block(activated_output, [256, 256, 1024])
    activated_output = identity_block(activated_output, [256, 256, 1024])
    activated_output = identity_block(activated_output, [256, 256, 1024])
    activated_output = identity_block(activated_output, [256, 256, 1024])
    activated_output = identity_block(activated_output, [256, 256, 1024])
    activated_output = identity_block(activated_output, [256, 256, 1024])

    activated_output = projection_block(activated_output, [512, 512, 2048])
    activated_output = identity_block(activated_output, [512, 512, 2048])
    activated_output = identity_block(activated_output, [512, 512, 2048])

    output_layer = K.layers.AveragePooling2D(
        pool_size=(7, 7),
        strides=None,
        padding='same'
    )(activated_output)

    output = K.layers.Dense(
        units=1000,
        activation='softmax',
        kernel_initializer=initializer_kernel_weights
    )(output_layer)

    model = K.Model(inputs=inputs, outputs=output)

    return model
