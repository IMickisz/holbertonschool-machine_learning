#!/usr/bin/env python3
""" Module that contains calculate_loss function """
import tensorflow.compat.v1 as tf


def calculate_loss(y, y_pred):
    """
    Function that calculates the softmax cross-entropy loss of a prediction
         - y : placeholder for the labels of the input data
         - y_pred : tensor containing the network’s predictions
    """
    loss = tf.losses.softmax_cross_entropy(y, logits=y_pred)
    return loss
