#!/usr/bin/env python3
""" Module that contains create_placeholders function """
import tensorflow.compat.v1 as tf


def create_placeholders(nx, classes):
    """
    Function that returns two placeholders, x and y, for the neural network
         - x : placeholder for the input data to the neural network
         - y : placeholder for the one-hot labels for the input data
    """
    x = tf.placeholder(tf.float32, shape=(None, nx), name='x')
    y = tf.placeholder(tf.float32, shape=(None, classes), name='y')
    return x, y
