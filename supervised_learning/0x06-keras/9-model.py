#!/usr/bin/env python3
""" Module  that contains save_model and load_model functions """
import tensorflow.keras as K


def save_model(network, filename):
    """
    Function that saves an entire model
        - network: model to save
        - filename: path of the file that the model should be saved to
    Return: None
    """
    network.save(filename)
    return None


def load_model(filename):
    """
    Function that loads an entire model
        - filename: path of the file that the model should be loaded to
    Return: the loaded model
    """
    model = K.models.load_model(filename)
    return model
