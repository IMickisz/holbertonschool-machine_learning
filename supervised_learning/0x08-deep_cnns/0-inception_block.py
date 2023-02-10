#!/usr/bin/env python3
""" Module that contains inception_block function"""
import tensorflow.keras as K


def inception_block(A_prev, filters):
    """
    Function that builds an inception block
        A_prev: output from the previous layer
        filters: tuple or list containing F1, F3R, F3,F5R, F5, FPP
            F1: number of filters in the 1x1 convolution
            F3R: number of filters in the 1x1 convolutionbefore the 3x3
                 convolution
            F3: number of filters in the 3x3 convolution
            F5R: number of filters in the 1x1 convolution before the 5x5
                 convolution
            F5: number of filters in the 5x5 convolution
            FPP: number of filters in the 1x1 convolution after the max pooling
    Return: concatenated output of the inception block
    """
    F1, F3R, F3, F5R, F5, FPP = filters

    L1 = K.layers.Conv2D(F1, (1, 1), padding='same', activation='relu')(A_prev)

    L2 = K.layers.Conv2D(
        F3R, (1, 1), padding='same', activation='relu')(A_prev)
    L2 = K.layers.Conv2D(F3, (3, 3), padding='same', activation='relu')(L2)

    # Convolutional layer with F5R kernels of shape 1x1 with same padding
    L3 = K.layers.Conv2D(
        F5R, (1, 1), padding='same', activation='relu')(A_prev)
    L3 = K.layers.Conv2D(F5, (5, 5), padding='same', activation='relu')(L3)

    L4 = K.layers.MaxPooling2D(
        pool_size=(3, 3), strides=(1, 1), padding='same')(A_prev)
    L4 = K.layers.Conv2D(FPP, (1, 1), padding='same', activation='relu')(L4)

    return K.layers.concatenate([L1, L2, L3, L4])
