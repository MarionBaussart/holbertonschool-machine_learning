#!/usr/bin/env python3
"""
module containing function precision
"""
import numpy as np


def precision(confusion):
    """
    function that calculates the precision for each class
        in a confusion matrix / proportion of the data points our model
        says was relevant actually were relevant
    Args:
        confusion: confusion numpy.ndarray of shape (classes, classes)
            where row indices represent the correct labels
            and column indices represent the predicted labels
                classes: number of classes
    Return: a numpy.ndarray of shape (classes,)
        containing the precision of each class
        precision = TP / (TP + FP)
    """
    classes_precision = np.zeros(shape=(confusion.shape[0],))

    for i in range(confusion.shape[0]):
        negatives = np.sum(confusion.T[i])
        TP = confusion[i][i]
        FP = negatives - TP
        classes_precision[i] = TP / (TP + FP)

    return classes_precision
