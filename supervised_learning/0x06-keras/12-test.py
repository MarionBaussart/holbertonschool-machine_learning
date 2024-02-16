#!/usr/bin/env python3
"""
module containing function test_model
"""
import tensorflow.keras as K


def test_model(network, data, labels, verbose=True):
    """
    function that tests a neural network
    Args:
        network: network model to test
        data: input data to test the model with
        labels: correct one-hot labels of data
        verbose: boolean that determines if output should be printed
            during the testing process
    Return: the loss and accuracy of the model with the testing data
    """
    results = network.evaluate(x=data, y=labels, verbose=verbose)
    return results
