#!/usr/bin/env python3
""" Module that contains one_hot function """
import tensorflow.keras as K


def one_hot(labels, classes=None):
    """ Function that converts a label vector into a one-hot matrix """
    one_hot_labels = K.utils.to_categorical(labels, num_classes=classes,
                                            dtype='float32')
    return one_hot_labels
