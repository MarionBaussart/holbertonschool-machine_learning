#!/usr/bin/env python3
"""
module containing function lenet5
"""
import tensorflow.keras as K


def lenet5(X):
    """
    function that builds a modified version of the LeNet-5 architecture
        using keras
    Args:
        X: K.Input of shape (m, 28, 28, 1) containing the input images
            for the network
                m: number of images
    Return:
        K.Model compiled to use Adam optimization
            (with default hyperparameters) and accuracy metrics
    """
    initializer_kernel_weights = K.initializers.HeNormal(seed=None)

    # Convolutional layer with 6 kernels of shape 5x5 with same padding
    convolutional_layer_1 = K.layers.Conv2D(
        filters=6,
        kernel_size=(5, 5),
        padding='same',
        activation='relu',
        kernel_initializer=initializer_kernel_weights
    )
    output = convolutional_layer_1(X)

    # Max pooling layer with kernels of shape 2x2 with 2x2 strides
    max_pooling_layer_1 = K.layers.MaxPooling2D(
        pool_size=(2, 2),
        strides=(2, 2)
    )
    output = max_pooling_layer_1(output)

    # Convolutional layer with 16 kernels of shape 5x5 with valid padding
    convolutional_layer_2 = K.layers.Conv2D(
        filters=16,
        kernel_size=(5, 5),
        padding='valid',
        activation='relu',
        kernel_initializer=initializer_kernel_weights
    )
    output = convolutional_layer_2(output)

    # Max pooling layer with kernels of shape 2x2 with 2x2 strides
    max_pooling_layer_2 = K.layers.MaxPooling2D(
        pool_size=(2, 2),
        strides=(2, 2)
    )
    output = max_pooling_layer_2(output)

    # flatten
    output = K.layers.Flatten()(output)

    # Fully connected layer with 120 nodes
    fully_connected_layer_1 = K.layers.Dense(
        units=120,
        activation='relu',
        kernel_initializer=initializer_kernel_weights
    )
    output = fully_connected_layer_1(output)

    # Fully connected layer with 84 nodes
    fully_connected_layer_2 = K.layers.Dense(
        units=84,
        activation='relu',
        kernel_initializer=initializer_kernel_weights
    )
    output = fully_connected_layer_2(output)

    # Fully connected softmax output layer with 10 nodes
    fully_connected_layer_3 = K.layers.Dense(
        units=10,
        activation='softmax',
        kernel_initializer=initializer_kernel_weights
    )
    output = fully_connected_layer_3(output)

    # build keras model and set Adam optimization
    # and accuracy metrics
    model = K.Model(inputs=X, outputs=output)
    optimizer = K.optimizers.Adam()
    model.compile(optimizer=optimizer,
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])

    return model
