#!/usr/bin/env python3
""" Module that contains a new function """


def poly_derivative(poly):
    """ Function that calculates the derivative of a polynomial """
    if (type(poly) is not list) or poly == []:
        return None
    elif len(poly) < 2:
        return [0]
    else:
        deriv_poly = [poly[i] * i for i in range(1, len(poly))]
        return deriv_poly
