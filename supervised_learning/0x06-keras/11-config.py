#!/usr/bin/env python3
"""
module containing function save_config and load_config
"""
import tensorflow.keras as K


def save_config(network, filename):
    """
    function that saves a model's configuration in JSON format
    Args:
        network: model whose configuration should be saved
        filename: path of the file that the configuration should be saved to
    Return: None
    """
    network_json = network.to_json()
    with open(filename, "w") as json_file:
        json_file.write(network_json)

    return None


def load_config(filename):
    """
    function that loads a model with a specific configuration
    Args:
        filename: path of the file containing the model's configuration
            in JSON format
    Return: None
    """
    with open(filename, 'r') as json_file:
        loaded_model_json = json_file.read()
        json_file.close()
    loaded_model = K.models.model_from_json(loaded_model_json)

    return loaded_model
