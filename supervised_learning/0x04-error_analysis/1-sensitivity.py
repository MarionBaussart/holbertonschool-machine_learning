#!/usr/bin/env python3
"""
module containing function sensitivity
"""
import numpy as np


def sensitivity(confusion):
    """
    function that calculates the sensitivity for each class
        in a confusion matrix / percentage of the positive which was
        correctly identified
    Args:
        confusion: confusion numpy.ndarray of shape (classes, classes)
            where row indices represent the correct labels
            and column indices represent the predicted labels
                classes: number of classes
    Return: a numpy.ndarray of shape (classes,)
        containing the sensitivity of each class
        sensitivity = TP / (TP + FN) = recall
    """
    classes_sensivity = np.zeros(shape=(confusion.shape[0],))

    for i in range(confusion.shape[0]):
        positives = np.sum(confusion[i])
        TP = confusion[i][i]
        FN = positives - TP
        classes_sensivity[i] = TP / (TP + FN)

    return classes_sensivity
