#!/usr/bin/env python3
"""
module containing function save_model and load_model
"""
import tensorflow.keras as K


def save_model(network, filename):
    """
    function that saves an entire model
    Args:
        network: model to save
        filename: path of the file that the model should be saved to
    Return: None
    """
    network.save(filename)
    return None


def load_model(filename):
    """
    function that loads an entire model
    Args:
        filename: path of the file that the model should be loaded to
    Return: the loaded model
    """
    model = K.models.load_model(filename)
    return model
