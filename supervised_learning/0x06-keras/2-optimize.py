#!/usr/bin/env python3
""" Module that contains optimize_model function """
import tensorflow.keras as K


def optimize_model(network, alpha, beta1, beta2):
    """
    Function that sets up Adam optimization for a keras model with
    categorical crossentropy loss and accuracy metrics:
        - network: model to optimize
        - alpha: learning rate
        - beta1: first Adam optimization parameter
        - beta2: second Adam optimization parameter
    """
    optimizer = K.optimizers.Adam(learning_rate=alpha, beta_1=beta1,
                                  beta_2=beta2, name='Adam')
    network.compile(optimizer=optimizer, loss='categorical_crossentropy',
                    metrics=['accuracy'])
    return
