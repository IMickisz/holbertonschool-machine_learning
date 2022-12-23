#!/usr/bin/env python3
""" Module that contains a new function """


def poly_integral(poly, C=0):
    """ Function that calculates the integral of a polynomial """
    if type(poly) is not list or len(poly) == 0 or type(C) is not int:
        return None
    if poly == [0]:
        return [C]
    exponent = 0
    for i in range(len(poly)):
        if type(poly[i]) is int or type(poly[i]) is float:
            exponent += 1
            number = poly[i] / exponent
            poly[i] = int(number) if number % 1 == 0 else number
        else:
            return None
    poly.insert(0, C)
    return poly
