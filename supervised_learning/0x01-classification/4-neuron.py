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
            - X : a np array with shape (nx, m) that contains the input data
        """
        preactivation = np.matmul(self.__W, X) + self.__b
        self.__A = 1 / (1 + np.exp(-preactivation))
        return self.__A

    def cost(self, Y, A):
        """
         Method that calculates the cost of the model using logistic regression
            - Y : a np array with shape (1, m) with correct labels
            - A : a np array with shape (1, m) containing the activated output
        """
        cost = Y * np.log(A) + (1 - Y) * np.log(1.0000001 - A)
        cost = np.sum(cost)
        cost = - cost / A.shape[1]
        return cost

    def evaluate(self, X, Y):
        """
        Method that evaluates the neuron’s predictions
            - X : a np array with shape (nx, m) that contains the input data
            - Y : a np array with shape (1, m) with correct labels
        """
        self.forward_prop(X)
        prediction = np.where(self.__A >= 0.5, 1, 0)
        cost = self.cost(Y, self.__A)
        return prediction, cost
