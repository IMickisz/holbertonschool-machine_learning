#!/usr/bin/env python3
""" Module that contains the Poisson class """


class Poisson:
    """ Class  that represents a poisson distribution """

    def __init__(self, data=None, lambtha=1.):
        """
        Class constructor
           - data is a list of the data to be used to estimate the distribution
           - lambtha is the expected number of occurences in a given time frame
        """
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            else:
                self.lambtha = float(lambtha)
        else:
            if type(data) != list:
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            else:
                self.lambtha = float(sum(data) / len(data))

    def pmf(self, k):
        """
        Instance method that calculates the value of the PMF for a given number
        of “successes”
           - k: number of “successes”
        Return: the PMF value for k
        """
        if type(k) != int:
            k = int(k)
        if k < 0:
            return 0
        e = 2.7182818285
        k_factorial = 1
        for i in range(2, k + 1):
            k_factorial *= i
        pmf = ((e ** (- self.lambtha)) * (self.lambtha ** k)) / k_factorial
        return pmf

    def cdf(self, k):
        """
        Instance method that calculates the value of the CDF for a given
        number of “successes”
           - k: number of “successes”
        Return: the CDF value for k
        """
        if type(k) != int:
            k = int(k)
        if k < 0:
            return 0
        cdf = 0
        for i in range(k + 1):
            cdf += self.pmf(i)
        return cdf
