#!/usr/bin/env python3
"""
module containing function f1_score
"""
import numpy as np
sensitivity = __import__('1-sensitivity').sensitivity
precision = __import__('2-precision').precision


def f1_score(confusion):
    """
    function that calculates the F1 score of a confusion matrix /
        From all the classes, how many of them we have predicted correctly
    Args:
        confusion: confusion numpy.ndarray of shape (classes, classes)
            where row indices represent the correct labels
            and column indices represent the predicted labels
                classes: number of classes
    Return: a numpy.ndarray of shape (classes,)
        containing the F1 score of each class
        F1 score = 2((precision * recall) / (precision + recall))
            with recall = sensitivity
    """
    classes_F1_score = np.zeros(shape=(confusion.shape[0],))
    CP = precision(confusion)
    CS = sensitivity(confusion)

    for i in range(len(classes_F1_score)):
        classes_F1_score[i] = 2 * ((CP[i] * CS[i]) / (CP[i] + CS[i]))

    return classes_F1_score
