#!/usr/bin/env python3
""" Module that contains pool function """
import numpy as np


def pool(images, kernel_shape, stride, mode='max'):
    """ Function that performs pooling on images
    - images: numpy.ndarray with shape (m, h, w, c) containing multiple
    images
        m is the number of images
        h is the height in pixels of the images
        w is the width in pixels of the images
        c is the number of channels in the image
    - kernel_shape: tuple of (kh, kw) containing the kernel shape for the
    pooling
        kh is the height of the kernel
        kw is the width of the kernel
    - stride: tuple of (sh, sw)
        sh is the stride for the height of the image
        sw is the stride for the width of the image
    - mode indicates the type of pooling
        max indicates max pooling
        avg indicates average pooling
    """
    m, h, w, c = images.shape
    kh, kw = kernel_shape
    sh, sw = stride

    if mode == "max":
        op = np.amax
    else:
        op = np.average
    p_h, p_w = 0, 0
    W_out = (w + (2 * p_w) - kw) // sw + 1
    H_out = (h + (2 * p_h) - kh) // sh + 1
    output_matrix = np.zeros((m, H_out, W_out, c))
    for h in range(H_out):
        for w in range(W_out):
            output_matrix[:, h, w, :] = op(
                images[:, sh*h: sh*h+kh, sw*w:sw*w+kw, :], axis=(1, 2))
    return output_matrix
