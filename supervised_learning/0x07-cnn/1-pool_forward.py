#!/usr/bin/env python3
""" Module that contains pool_forward function"""
import numpy as np


def pool_forward(A_prev, kernel_shape, stride=(1, 1), mode='max'):
    """
    Function that performs forward propagation over a pooling layer
    of a neural network
         - A_prev: numpy.ndarray of shape (m, h_prev, w_prev, c_prev)
            containing the output of the previous layer
                m: number of examples
                h_prev: height of the previous layer
                w_prev: width of the previous layer
                c_prev: number of channels in the previous layer
        - kernel_shape: tuple of (kh, kw) containing the size of the kernel
            for the pooling
                kh: filter height
                kw: filter width
        - stride: tuple of (sh, sw) containing the strides for the pooling
            sh: stride for the height
            sw: stride for the width
            mode: string containing either max or avg,
                indicating whether to perform maximum or average pooling
    """
    m, h_prev, w_prev, c_prev = A_prev.shape
    kh, kw = kernel_shape
    sh, sw = stride

    # pooled image shape
    pooled_image_h = ((h_prev - kh) / sh) + 1
    if int(pooled_image_h) > pooled_image_h:
        pooled_image_h = int(pooled_image_h) - 1
    else:
        pooled_image_h = int(pooled_image_h)

    pooled_image_w = ((w_prev - kw) / sw) + 1
    if int(pooled_image_w) > pooled_image_w:
        pooled_image_w = int(pooled_image_w) - 1
    else:
        pooled_image_w = int(pooled_image_w)

    # pooling
    pooled_images = np.zeros(shape=(m, pooled_image_h, pooled_image_w, c_prev))

    for height in range(pooled_image_h):
        for width in range(pooled_image_w):
            if mode == 'max':
                pooled_image = np.nanmax(
                    A_prev[:, height * sh:height * sh + kh,
                           width * sw:width * sw + kw],
                    axis=(1, 2))
                pooled_images[:, height, width] = pooled_image
            if mode == 'avg':
                pooled_image = np.nanmean(
                    A_prev[:, height * sh:height * sh + kh,
                           width * sw:width * sw + kw],
                    axis=(1, 2))
                pooled_images[:, height, width] = pooled_image

    return pooled_images
