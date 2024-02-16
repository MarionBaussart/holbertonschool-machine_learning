#!/usr/bin/env python3
"""
module containing function create_confusion_matrix
"""
import numpy as np


def create_confusion_matrix(labels, logits):
    """
    function that creates a confusion matrix
    Args:
        labels: one-hot numpy.ndarray of shape (m, classes)
            containing the correct labels for each data point
                m: number of data points
                classes: number of classes
        logits: one-hot numpy.ndarray of shape (m, classes)
            containing the predicted labels
    Return: a confusion numpy.ndarray of shape (classes, classes)
        with row indices representing the correct labels
        and column indices representing the predicted labels
    """
    confusion = np.zeros(shape=(labels.shape[1], logits.shape[1]))

    labels_index = np.argmax(labels, axis=1)
    logits_index = np.argmax(logits, axis=1)

    for index, label_index in enumerate(labels_index):
        confusion[label_index][logits_index[index]] += 1

    return confusion
