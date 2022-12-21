#!/usr/bin/env python3
""" Module that contains new a function """


def cat_matrices2D(mat1, mat2, axis=0):
    """ Function that concatenates two matrices along a specific axis """
    if len(mat1[0]) == len(mat2[0]) and axis == 0:
        matrix = [ele.copy() for ele in mat1]
        matrix += [ele.copy() for ele in mat2]
        return matrix
    elif len(mat1) == len(mat2) and axis == 1:
        matrix = [mat1[j] + mat2[j] for j in range(len(mat1))]
        return matrix
    else:
        return None


def add_arrays(arr1, arr2):
    """ Function that adds two arrays element-wise """
    if len(arr1) != len(arr2):
        return None
    list = []
    for i in range(len(arr1)):
        list.append(arr1[i] + arr2[i])
    return list


def matrix_shape(matrix):
    """ Function that calculates the shape of a matrix """
    if type(matrix[0]) is not list:
        return [len(matrix)]
    else:
        return [len(matrix)] + matrix_shape(matrix[0])
