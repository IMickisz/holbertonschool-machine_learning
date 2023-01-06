#!/usr/bin/env python3
""" Module that contains create_layer function """
import tensorflow.compat.v1 as tf


def create_layer(prev, n, activation):
    """
    Function that returns two placeholders, x and y, for the neural network
         - prev : tensor output of the previous layer
         - n : number of nodes in the layer to create
         - activation : activation function that the layer should use
    """
    k_init = tf.keras.initializers.VarianceScaling(mode='fan_avg')
    layer = tf.layers.Dense(units=n, activation=activation,
                            kernel_initializer=k_init, name='layer')
    return layer(prev)
