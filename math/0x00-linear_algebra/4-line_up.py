#!/usr/bin/env python3
""" Module that contains new a function """


def add_arrays(arr1, arr2):
    """ Function that adds two arrays element-wise """
    if len(arr1) != len(arr2):
        return None
    list = []
    for i in range(len(arr1)):
        list.append(arr1[i] + arr2[i])
    return list
