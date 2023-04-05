#!/usr/bin/env python3trans
""" Module that contains poly_integral function """


def poly_integral(poly, C=0):
    """ Function that calculates the integral of a polynomial """
    if type(poly) != list or len(poly) == 0 or type(C) != int:
        return None

    if poly == [0]:
        return [C]

    integral = [C]
    for i in range(len(poly)):
        if (poly[i] / (i + 1)) % 1 == 0:
            integral.append(int(poly[i] / (i + 1)))
        else:
            integral.append(poly[i] / (i + 1))
    return integral
