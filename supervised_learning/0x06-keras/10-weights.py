#!/usr/bin/env python3
"""
module containing function save_weights and load_weights
"""
import tensorflow.keras as K


def save_weights(network, filename, save_format='h5'):
    """
    function that saves a model's weights
    Args:
        network: model whose weights should be saved
        filename: path of the file that the weights should be saved to
        save_format: format in which the weights should be saved
    Return: None
    """
    network.save_weights(filename, save_format=save_format)
    return None


def load_weights(network, filename):
    """
    function that loads a model's weights
    Args:
        network: model to which the weights should be loaded
        filename: path of the file that the weights should be loaded from
    Return: None
    """
    network.load_weights(filename)
    return None
