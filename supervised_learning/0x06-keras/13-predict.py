#!/usr/bin/env python3
"""
module containing function predict
"""
import tensorflow.keras as K


def predict(network, data, verbose=False):
    """
    function that makes a prediction using a neural network
    Args:
        network: network model to make the prediction with
        data: input data to make the prediction with
        verbose: boolean that determines if output should be printed
            during the prediction process
    Return: the prediction for the data
    """
    prediction = network.predict(data, verbose=verbose)
    return prediction
