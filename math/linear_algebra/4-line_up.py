#!/usr/bin/env python3
""" Module that contains add_arrays function """


def add_arrays(arr1, arr2):
    """ Function that adds two arrays element-wise """
    if len(arr1) != len(arr2):
        return None
    result = [arr1[i] + arr2[i] for i in range(len(arr1))]
    return result
