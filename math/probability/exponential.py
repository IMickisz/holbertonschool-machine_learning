#!/usr/bin/env python3
""" Module that contains the exponential class """
e = 2.7182818285


class Exponential:
    """ Class that represents an exponential distribution """

    def __init__(self, data=None, lambtha=1.):
        """ Class contructor  """
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            else:
                self.lambtha = float(lambtha)
        else:
            if type(data) != list:
                raise TypeError("data must be a list")
            elif len(data) < 2:
                raise ValueError("data must contain multiple values")
            else:
                mean = sum(data) / len(data)
                self.lambtha = float(1 / mean)

    def pdf(self, x):
        """ Instance method that calculate the PDF for a given time period """
        if x < 0:
            return 0
        pdf = self.lambtha * (e ** (- self.lambtha * x))
        return pdf

    def cdf(self, x):
        """ Instance method that calculate the CDF for a given time period """
        if x < 0:
            return 0
        cdf = 1 - (e ** (- self.lambtha * x))
        return cdf
