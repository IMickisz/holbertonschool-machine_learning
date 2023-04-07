#!/usr/bin/env python3
""" Module that contains the normal class """
e = 2.7182818285
π = 3.1415926536


class Normal:
    """ Class that represents an normal distribution """

    def __init__(self, data=None, mean=0., stddev=1.):
        """ Class contructor """
        if data is None:
            if stddev <= 0:
                raise ValueError("stddev must be a positive value")
            else:
                self.mean = float(mean)
                self.stddev = float(stddev)
        else:
            if type(data) != list:
                raise TypeError("data must be a list")
            elif len(data) < 2:
                raise ValueError("data must contain multiple values")
            else:
                self.mean = float(sum(data) / len(data))
                stddev_term = 0
                for i in range(len(data)):
                    stddev_term += (data[i] - self.mean) ** 2
                self.stddev = float((stddev_term / len(data)) ** (1 / 2))

    def z_score(self, x):
        """ Instance method that calculate z-score of a given x-value """
        return (x - self.mean) / self.stddev

    def x_value(self, z):
        """ Instance method that calculate x-value of a given z-score """
        return (z * self.stddev) + self.mean

    def pdf(self, x):
        """ Instance method that calculates the value of the PDF for a given
        x-value """
        racine = (2 * π * self.stddev ** 2) ** (- 1 / 2)
        exponent = (- 1 / 2) * (((x - self.mean) ** 2) / (self.stddev ** 2))
        return racine * (e ** (exponent))

    def cdf(self, x):
        """ Instance method that calculates the value of the CDF for a given
        time period """
        arg = (x - self.mean) / (self.stddev * (2 ** (1 / 2)))
        factor = 2 / (π ** (1 / 2))
        integral = (arg - ((arg ** 3) / 3) + ((arg ** 5) / 10) -
                    ((arg ** 7) / 42) + ((arg ** 9) / 216))
        erf = factor * integral
        cdf = (1 / 2) * (1 + erf)
        return cdf
