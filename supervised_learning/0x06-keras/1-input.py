#!/usr/bin/env python3
"""
module containing function build_model
"""
import tensorflow.keras as K


def build_model(nx, layers, activations, lambtha, keep_prob):
    """
    function that builds a neural network with the Keras library
        using Input class
    Args:
        nx: number of input features to the network
        layers: list containing the number of nodes in each layer
            of the network
        activations: list containing the activation functions used
            for each layer of the network
        lambtha: L2 regularization parameter
        keep_prob: probability that a node will be kept for dropout
    Return: the keras model
    """
    inputs = K.Input(shape=(nx,))
    for i in range(len(layers)):
        if i == 0:
            output = K.layers.Dense(
                layers[i],
                activation=activations[i],
                kernel_regularizer=K.regularizers.L2(lambtha)
            )(inputs)
        else:
            output = K.layers.Dropout(1 - keep_prob)(output)
            output = K.layers.Dense(
                layers[i],
                activation=activations[i],
                kernel_regularizer=K.regularizers.L2(lambtha)
            )(output)
    model = K.Model(inputs=inputs, outputs=output)

    return model
