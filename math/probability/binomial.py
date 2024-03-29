#!/usr/bin/env python3
""" Module that contains the Binomial class """


class Binomial:
    """ Class that represents a binomial distribution """

    def __init__(self, data=None, n=1, p=0.5):
        """ Class contructor """
        if data is None:
            if n <= 0:
                raise ValueError("n must be a positive value")
            if p <= 0 or p >= 1:
                raise ValueError("p must be greater than 0 and less than 1")
            else:
                self.n = int(n)
                self.p = float(p)
        else:
            if type(data) != list:
                raise TypeError("data must be a list")
            elif len(data) < 2:
                raise ValueError("data must contain multiple values")
            else:
                mean = sum(data) / len(data)
                somme = 0
                for i in range(len(data)):
                    somme += (data[i] - mean) ** 2
                variance = somme / len(data)
                q = variance / mean
                p = 1 - q
                n = round(mean / p)
                p = mean / n
                self.p = float(p)
                self.n = round(n)

    def factorial(self, n):
        """ Instance method that calculate the factorial for a number n > 0 """
        factorial = 1

        for i in range(2, n + 1):
            factorial *= i
        return factorial

    def pmf(self, k):
        """ Instance method that calculates the PDF for a given number of
        “successes” """
        if k < 0:
            return 0
        if k <= self.n:
            k = int(k)

            binomial_coeff = self.factorial(self.n) / \
                (self.factorial(k) * self.factorial(self.n - k))
            pmf = binomial_coeff * (self.p ** k) * \
                ((1 - self.p) ** (self.n - k))
            return pmf
        else:
            return 0

    def cdf(self, k):
        """ Instance method that calculate the CDF for a given number of
        “successes” """
        if k < 0:
            return 0
        if k <= self.n:
            k = int(k)
            cdf = 0
            for i in range(k + 1):
                cdf += self.pmf(i)
            return cdf
        else:
            return 0
