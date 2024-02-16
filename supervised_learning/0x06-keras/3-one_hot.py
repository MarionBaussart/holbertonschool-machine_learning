#!/usr/bin/env python3
"""
module containing function one_hot
"""
import tensorflow.keras as K


def one_hot(labels, classes=None):
    """
    function that converts a label vector into a one-hot matrix
    Args:
        labels: label vector to convert
        classes: number of classes in labels
    Return: the one-hot matrix
    """
    one_hot_labels = K.utils.to_categorical(labels,
                                            num_classes=classes,
                                            dtype='float32')

    return one_hot_labels
