#!/usr/bin/env python3
""" Module that contains convolve_grayscale_same function """
import numpy as np


def convolve_grayscale_same(images, kernel):
    """ Function that performs a same convolution on grayscale images
    - images: numpy.ndarray with shape (m, h, w) containing multiple grayscale
    images
        m is the number of images
        h is the height in pixels of the images
        w is the width in pixels of the images
    - kernel: numpy.ndarray with shape (kh, kw) containing the kernel for the
    convolution
        kh is the height of the kernel
        kw is the width of the kernel
    """
    m, h, w = images.shape
    kh, kw = kernel.shape

    if kh % 2 != 0 and kw % 2 != 0:
        p_h = (kh - 1) // 2
        p_w = (kw - 1) // 2
    else:
        p_h = kh // 2
        p_w = kw // 2

    p_images = np.pad(images, ((0, 0), (p_h, p_h), (p_w, p_w)), 'constant')
    output_matrix = np.zeros((m, h, w))
    for i in range(w):
        for j in range(h):
            part_image = p_images[:, j:j + kh, i:i + kw]
            output_matrix[:, j, i] = np.tensordot(part_image, kernel, axes=2)
    return output_matrix
