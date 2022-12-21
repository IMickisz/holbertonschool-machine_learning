#!/usr/bin/env python3
""" Module that contain a new function """


def mat_mul(mat1, mat2):
    """ Function that performs matrix multiplication """
    if matrix_shape(mat1)[1] != matrix_shape(mat2)[0]:
        return None
    matrix = []
    for i in range(len(mat1)):
        line = []
        for j in range(len(mat2[0])):
            element = 0
            for k in range(len(mat1[0])):
                element = element + mat1[i][k] * mat2[k][j]
            line.append(element)
        matrix.append(line)
    return matrix


def matrix_shape(matrix):
    """ Function that calculates the shape of a matrix """
    shape = []
    shape.append(len(matrix))
    shape.append(len(matrix[0]))
    if type(matrix[0][0]) == list:
        shape.append(len(matrix[0][0]))
    return shape
