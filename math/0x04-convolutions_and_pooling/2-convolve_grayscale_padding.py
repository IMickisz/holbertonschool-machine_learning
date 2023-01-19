#!/usr/bin/env python3
""" Module that contains convolve_grayscale_padding function """
import numpy as np


def convolve_grayscale_padding(images, kernel, padding):
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
    - padding: tuple of (ph, pw)
        ph is the padding for the height of the image
        pw is the padding for the width of the image
        the image should be padded with 0’s
    """
    m, h, w = images.shape
    kh, kw = kernel.shape
    p_h, p_w = padding

    p_images = np.pad(images, ((0, 0), (p_h, p_h), (p_w, p_w)), 'constant')
    W_out = w - kw + 1 + (2 * p_w)
    H_out = h - kh + 1 + (2 * p_h)
    output_matrix = np.zeros((m, H_out, W_out))
    for i in range(W_out):
        for j in range(H_out):
            part_image = p_images[:, j:j + kh, i:i + kw]
            output_matrix[:, j, i] = np.tensordot(part_image, kernel, axes=2)
    return output_matrix
