#!/usr/bin/env python3
""" Module  that contains save_weight and load_weight functions """
import tensorflow.keras as K


def save_weights(network, filename, save_format='h5'):
    """
    Function that saves a model’s weights
        - network: model whose weights should be saved
        - filename: path of the file that the weights should be saved to
        - save_format: format in which the weights should be saved
    Returns: None
    """
    network.save_weights(filename, save_format=save_format)
    return None


def load_model(filename):
    """
    Function that loads a model’s weights
        - network: model to which the weights should be loaded
        - filename: path of the file that the weights should be loaded from
    Returns: None
    """
    network.load_weights(filename)
    return None
