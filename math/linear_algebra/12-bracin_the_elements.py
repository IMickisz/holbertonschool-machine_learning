#!/usr/bin/env python3
""" Module that contains np_shape function"""


def np_elementwise(mat1, mat2):
    """ Function that performs element-wise addition, subtraction,
    multiplication, and division """
    return (mat1 + mat2, mat1 - mat2, mat1 * mat2, mat1 / mat2)
