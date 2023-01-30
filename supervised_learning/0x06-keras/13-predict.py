#!/usr/bin/env python3
""" Module that contains predict function"""
import tensorflow.keras as K


def predict(network, data, verbose=False):
    """
    Function that makes a prediction using a neural network
        - network: network model to make the prediction with
        - data: input data to make the prediction with
        - verbose: boolean that determines if output should be printed during
    the testing process
    Returns:  the prediction for the data
    """
    prediction = network.predict(data, verbose=verbose)
    return prediction
