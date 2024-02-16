#!/usr/bin/env python3
"""
module containing function lenet5
"""
import tensorflow.compat.v1 as tf


def lenet5(x, y):
    """
    function that builds a modified version of the LeNet-5 architecture
        using tensorflow
    Args:
        x: tf.placeholder of shape (m, 28, 28, 1) containing the input images
            for the network
                m: number of images
        y: tf.placeholder of shape (m, 10) containing the one-hot labels
            for the network
    Return:
        tensor for the softmax activated output,
        training operation that utilizes Adam optimization
            (with default hyperparameters),
        tensor for the loss of the netowrk,
        tensor for the accuracy of the network
    """
    initializer_kernel_weights = tf.keras.initializers.VarianceScaling(
        scale=2.0)

    # Convolutional layer with 6 kernels of shape 5x5 with same padding
    convolutional_layer_1 = tf.layers.Conv2D(
        filters=6,
        kernel_size=(5, 5),
        padding='same',
        activation='relu',
        kernel_initializer=initializer_kernel_weights
    )
    output = convolutional_layer_1(x)

    # Max pooling layer with kernels of shape 2x2 with 2x2 strides
    max_pooling_layer_1 = tf.layers.MaxPooling2D(
        pool_size=(2, 2),
        strides=(2, 2)
    )
    output = max_pooling_layer_1(output)

    # Convolutional layer with 16 kernels of shape 5x5 with valid padding
    convolutional_layer_2 = tf.layers.Conv2D(
        filters=16,
        kernel_size=(5, 5),
        padding='valid',
        activation='relu',
        kernel_initializer=initializer_kernel_weights
    )
    output = convolutional_layer_2(output)

    # Max pooling layer with kernels of shape 2x2 with 2x2 strides
    max_pooling_layer_2 = tf.layers.MaxPooling2D(
        pool_size=(2, 2),
        strides=(2, 2)
    )
    output = max_pooling_layer_2(output)

    # flatten
    output = tf.layers.Flatten()(output)

    # Fully connected layer with 120 nodes
    fully_connected_layer_1 = tf.layers.Dense(
        units=120,
        activation='relu',
        kernel_initializer=initializer_kernel_weights
    )
    output = fully_connected_layer_1(output)

    # Fully connected layer with 84 nodes
    fully_connected_layer_2 = tf.layers.Dense(
        units=84,
        activation='relu',
        kernel_initializer=initializer_kernel_weights
    )
    output = fully_connected_layer_2(output)

    # Fully connected softmax output layer with 10 nodes
    fully_connected_layer_3 = tf.layers.Dense(
        units=10,
        kernel_initializer=initializer_kernel_weights
    )
    output = fully_connected_layer_3(output)

    # get tensors for return
    softmax = tf.nn.softmax(output)
    loss = tf.losses.softmax_cross_entropy(y, output)
    adam_operation = tf.train.AdamOptimizer().minimize(loss)

    y_tensor = tf.argmax(y, axis=1)
    y_pred_tensor = tf.argmax(output, axis=1)
    correct_predictions = tf.math.equal(y_tensor, y_pred_tensor)
    accuracy = tf.reduce_mean(tf.cast(correct_predictions, tf.float32))

    return softmax, adam_operation, loss, accuracy
