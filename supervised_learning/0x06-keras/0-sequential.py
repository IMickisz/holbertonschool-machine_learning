#!/usr/bin/env python3
""" Module that contains build_model function """
import tensorflow.keras as K


def build_model(nx, layers, activations, lambtha, keep_prob):
    """
    Function that builds a neural network with the Keras library
        - nx: number of input features to the network
        - layers: list containing the number of nodes in each layer of the
    network
        - activations: list containing the activation functions used for each
    layer of the network
        - lambtha: L2 regularization parameter
        - keep_prob: probability that a node will be kept for dropout
    You are not allowed to use the Input class
    """
    model = K.Sequential()
    for i in range(len(layers)):
        if i == 0:
            model.add(K.layers.Dense(
                layers[i], input_shape=(nx,),
                activation=activations[i],
                kernel_regularizer=K.regularizers.L2(lambtha)))
        else:
            model.add(K.layers.Dropout(1 - keep_prob))
            model.add(K.layers.Dense(
                layers[i], activation=activations[i],
                kernel_regularizer=K.regularizers.L2(lambtha)))

    return model
