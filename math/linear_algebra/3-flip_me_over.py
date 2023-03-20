#!/usr/bin/env python3
""" Module that contains matrix_transpose function """


def matrix_transpose(matrix):
    """ Function that returns the transpose of a 2D matrix """
    matrix_t = []
    for i in range(len(matrix[0])):
        row = []
        for item in matrix:
            row.append(item[i])
        matrix_t.append(row)
    return matrix_t
