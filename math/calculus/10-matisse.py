#!/usr/bin/env python3trans
""" Module that contains poly_derivative function """


def poly_derivative(poly):
    """ Function that calculates the derivative of a polynomial """
    if type(poly) != list or len(poly) == 0:
        return None

    if len(poly) == 1:
        return [0]

    derivate = []
    for i in range(1, len(poly)):
        derivate.append(poly[i] * i)
    return derivate
