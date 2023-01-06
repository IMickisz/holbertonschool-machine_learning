#!/usr/bin/env python3
""" Module that contains def forward_prop function """
import tensorflow.compat.v1 as tf
create_layer = __import__('1-create_layer').create_layer


def forward_prop(x, layer_sizes=[], activations=[]):
    """
    Function that creates the forward propagation graph for the neural network
         - x : placeholder for the input data
         - layer_sizes : list containing the number of nodes in each layer of
                         the network
         - activation : list containing the activation functions for each layer
                        of the network
    """
    for size, activation in zip(layer_sizes, activations):
        x = create_layer(x, size, activation)
    return x
