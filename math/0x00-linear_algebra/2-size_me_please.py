#!/usr/bin/env python3
""" Module that contain a new function """


def matrix_shape(matrix):
    """ Function that calculates the shape of a matrix """
    if type(matrix[0]) is not list:
        return [len(matrix)]
    else:
        return [len(matrix)] + matrix_shape(matrix[0])
