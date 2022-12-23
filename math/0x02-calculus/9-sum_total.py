#!/usr/bin/env python3
""" Module that contains a new function """


def summation_i_squared(n):
    """ Function that calculates the sum of i=1 until n of i² """
    if (type(n) is not int) or (n is None) or (n < 1):
        return None
    else:
        result = map(lambda i: i ** 2, range(1, n + 1))
        return sum(result)
