#!/usr/bin/env python3
"""
module containing function densenet121
"""
import tensorflow.keras as K
dense_block = __import__('5-dense_block').dense_block
transition_layer = __import__('6-transition_layer').transition_layer


def densenet121(growth_rate=32, compression=1.0):
    """
    function that builds the DenseNet-121 architecture
        as described in Densely Connected Convolutional Networks
    Args:
        growth_rate: growth rate
        compression: compression factor
    Return: the keras model
    """
    inputs = K.Input(shape=(224, 224, 3))

    initializer_kernel_weights = K.initializers.HeNormal(seed=None)

    batch_normalization = K.layers.BatchNormalization(axis=3)(inputs)
    activated_output = K.layers.Activation('relu')(batch_normalization)
    conv_7x7 = K.layers.Conv2D(
        filters=64,
        kernel_size=(7, 7),
        strides=(2, 2),
        padding='same',
        kernel_initializer=initializer_kernel_weights
    )(activated_output)
    max_pooling = K.layers.MaxPooling2D(
        pool_size=(3, 3),
        strides=(2, 2),
        padding='same'
    )(conv_7x7)

    DB_1, nb_filters = dense_block(max_pooling, 64, growth_rate, 6)
    TL_1, nb_filters = transition_layer(DB_1, nb_filters, compression)
    DB_2, nb_filters = dense_block(TL_1, nb_filters, growth_rate, 12)
    TL_2, nb_filters = transition_layer(DB_2, nb_filters, compression)
    DB_3, nb_filters = dense_block(TL_2, nb_filters, growth_rate, 24)
    TL_3, nb_filters = transition_layer(DB_3, nb_filters, compression)
    DB_4, nb_filters = dense_block(TL_3, nb_filters, growth_rate, 16)

    # classification layer
    average_pooling = K.layers.AveragePooling2D(
        pool_size=(7, 7),
        strides=None,
        padding='same'
    )(DB_4)

    output = K.layers.Dense(
        units=1000,
        activation='softmax',
        kernel_initializer=initializer_kernel_weights
    )(average_pooling)

    model = K.Model(inputs=inputs, outputs=output)

    return model
