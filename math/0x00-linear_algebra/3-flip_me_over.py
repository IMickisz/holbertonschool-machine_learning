#!/usr/bin/env python3
""" Module that contains new a function """


def matrix_transpose(matrix):
    """ Function to calculate the transpose of a 2D matrix """
    return [[matrix[i][j] for i in range(len(matrix))]
            for j in range(len(matrix[0]))]
