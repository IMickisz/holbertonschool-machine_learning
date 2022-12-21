#!/usr/bin/env python3
""" Module that contains new a function """


def add_matrices2D(mat1, mat2):
    """ Function that adds two matrices element-wise """
    if matrix_shape(mat1) != matrix_shape(mat2):
        return None
    mat = []
    for i in range(len(mat1)):
        mat.append(add_arrays(mat1[i], mat2[i]))
    return mat


def matrix_shape(matrix):
    """ Function that calculates the shape of a matrix """
    shape = []
    shape.append(len(matrix))
    shape.append(len(matrix[0]))
    if type(matrix[0][0]) == list:
        shape.append(len(matrix[0][0]))
    return shape


def add_arrays(arr1, arr2):
    """ Function that adds two arrays element-wise """
    if len(arr1) != len(arr2):
        return None
    list = []
    for i in range(len(arr1)):
        list.append(arr1[i] + arr2[i])
    return list
