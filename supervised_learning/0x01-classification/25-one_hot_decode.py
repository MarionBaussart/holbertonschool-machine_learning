#!/usr/bin/env python3
"""module that contains the one_hot_encode function"""
import numpy as np


def one_hot_decode(one_hot):
    """
    Converts a numeric label vector into a one-hot matrix
        Args:
            one_hot: a one-hot encoded numpy.ndarray with shape (classes, m)
                m: the number of examples
                classes: the maximum number of classes
        Return:
            a numpy.ndarray with shape (m, ) containing the numeric labels
                for each example, or None on failure
    """
    if type(one_hot) != np.ndarray or one_hot.ndim != 2:
        return None

    decode_one_hot = np.argmax(one_hot, axis=0)
    return decode_one_hot
