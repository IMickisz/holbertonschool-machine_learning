#!/usr/bin/env python3
""" Module that create a neuron """
import numpy as np


class Neuron:
    """ Class that defines a single neuron performing binary classification """

    def __init__(self, nx):
        """
        class constructor
           - nx: is the number of input features to the neuron
        """
        if type(nx) is not int:
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        self.__W = np.random.randn(1, nx)
        self.__b = 0
        self.__A = 0

    @property
    def W(self):
        """ Getter function for W that return the weight vector neuron """
        return self.__W

    @property
    def b(self):
        """ Getter function for b that return the  bias for the neuron """
        return self.__b

    @property
    def A(self):
        """ Getter function for A that return the activated output of the
        neuron """
        return self.__A

    def forward_prop(self, X):
        """
        Method that calculates the forward propagation of the neuron
            - X: a np array with shape (nx, m) that contains the input data
        """
        preactivation = np.matmul(self.__W, X) + self.__b
        self.__A = 1 / (1 + np.exp(-preactivation))
        return self.__A
