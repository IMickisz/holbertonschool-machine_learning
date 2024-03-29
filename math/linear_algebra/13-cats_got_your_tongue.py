#!/usr/bin/env python3trans
""" Module that contains np_cat function """
import numpy as np


def np_cat(mat1, mat2, axis=0):
    """ Function that concatenates two matrices along a specific axis """
    return np.concatenate((mat1, mat2), axis)
