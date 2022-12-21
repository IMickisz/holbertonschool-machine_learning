#!/usr/bin/env python3
""" Module that contains new a function """


def add_matrices2D(mat1, mat2):
    """ Function that adds two matrices element-wise """
    if len(mat1) != len(mat2):
        return None
    if len(mat1[0]) != len(mat2[0]):
        return None
    mat = []
    for i in range(len(mat1)):
        mat.append(add_arrays(mat1[i], mat2[i]))
    return mat
