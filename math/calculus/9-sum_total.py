#!/usr/bin/env python3trans
""" Module that contains the summation_i_squared function """


def summation_i_squared(n):
    """ Function that calculate the sum of i² """
    if type(n) == int and n >= 1:
        sum = (n * (n + 1) * ((2 * n) + 1)) / 6
        return int(sum)
    else:
        return None
