#!/usr/bin/env python3
""" Module that contains calculate_accuracy function """
import tensorflow.compat.v1 as tf


def calculate_accuracy(y, y_pred):
    """
    Function that calculates the accuracy of a prediction
         - y : placeholder for the labels of the input data
         - y_pred : tensor containing the network’s predictions
    """
    equality = tf.math.equal(tf.argmax(y_pred, axis=1), tf.argmax(y, axis=1))
    accuracy = tf.math.reduce_mean(tf.cast(equality, tf.float32))
    return accuracy
