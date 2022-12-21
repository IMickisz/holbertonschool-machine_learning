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


def add_arrays(arr1, arr2):
    """ Function that adds two arrays element-wise """
    if len(arr1) != len(arr2):
        return None
    list = []
    for i in range(len(arr1)):
        list.append(arr1[i] + arr2[i])
    return list
