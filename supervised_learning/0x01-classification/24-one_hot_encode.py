#!/usr/bin/env python3
"""module that contains the one_hot_encode function"""
import numpy as np


def one_hot_encode(Y, classes):
    """
    Converts a numeric label vector into a one-hot matrix
        Args:
            Y: numpy.ndarray with shape (m,) containing numeric class labels
                with m: the number of examples
            classes: the maximum number of classes found in Y
        Return:
            a one-hot encoding of Y with shape (classes, m), or None on failure
    """
    if type(Y) != np.ndarray or type(classes) != int or classes < Y.max():
        return None

    hot_Y = np.eye(classes)[Y].T
    if type(hot_Y) != np.ndarray:
        return None
    return hot_Y
