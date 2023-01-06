#!/usr/bin/env python3
""" Module that contains create_train_op function """
import tensorflow.compat.v1 as tf


def create_train_op(loss, alpha):
    """
    Function that creates the training operation for the network
         - loss : loss of the network’s prediction
         - alpha : learning rate
    """
    trainer = tf.train.GradientDescentOptimizer(learning_rate=alpha)
    return trainer.minimize(loss)
