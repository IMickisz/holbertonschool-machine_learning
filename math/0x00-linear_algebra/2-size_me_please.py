#!/usr/bin/env python3
""" Module that contain a new function """


def matrix_shape(matrix):
    """ Function that calculates the shape of a matrix """
    shape = []
    shape.append(len(matrix))
    shape.append(len(matrix[0]))
    if type(matrix[0][0]) == list:
        shape.append(len(matrix[0][0]))
    return shape
