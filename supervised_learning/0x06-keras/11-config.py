#!/usr/bin/env python3
""" Module that contains save_config and load_config functions """
import tensorflow.keras as K


def save_config(network, filename):
    """
    Function that saves a model's configuration in JSON format
        - network: model whose configuration should be saved
        - filename: path of the file that the configuration should be saved to
    Return: None
    """
    network_json = network.to_json()
    with open(filename, "w") as json_file:
        json_file.write(network_json)
    return None


def load_config(filename):
    """
    Function that loads a model with a specific configuration
        - filename: path of the file containing the model's configuration
            in JSON format
    Return: None
    """
    with open(filename, 'r') as json_file:
        loaded_model_json = json_file.read()
        json_file.close()
    loaded_model = K.models.model_from_json(loaded_model_json)
    return loaded_model
