#!/usr/bin/env python3
"""
module containing function specificity
"""
import numpy as np


def specificity(confusion):
    """
    function that calculates the specificity for each class
        in a confusion matrix / percentage of the negative target
        which was correctly identified
    Args:
        confusion: confusion numpy.ndarray of shape (classes, classes)
            where row indices represent the correct labels
            and column indices represent the predicted labels
                classes: number of classes
    Return: a numpy.ndarray of shape (classes,)
        containing the specificity of each class
        specificity = TN / (TN + FP)
    """
    classes_specificity = np.zeros(shape=(confusion.shape[0],))
    sum_all = np.sum(confusion)

    for i in range(confusion.shape[0]):
        positives = np.sum(confusion[i])
        negatives = np.sum(confusion.T[i])
        TP = confusion[i][i]
        FN = positives - TP
        FP = negatives - TP
        TN = sum_all - TP - FN - FP
        classes_specificity[i] = TN / (TN + FP)

    return classes_specificity
