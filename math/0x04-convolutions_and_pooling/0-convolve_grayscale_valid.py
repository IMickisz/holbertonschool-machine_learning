#!/usr/bin/env python3
""" Module that contains convolve_grayscale_valid function """
import numpy as np


def convolve_grayscale_valid(images, kernel):
    """ Function that performs a valid convolution on grayscale images
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
    W_out = w - kw + 1
    H_out = h - kh + 1

    output_matrix = np.zeros((m, H_out, W_out))
    for i in range(W_out):
        for j in range(H_out):
            part_image = images[:, j:j + kh, i:i + kw]
            output_matrix[:, j, i] = np.tensordot(part_image, kernel, axes=2)
    return output_matrix
