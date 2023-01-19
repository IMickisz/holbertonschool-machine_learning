#!/usr/bin/env python3
""" Module that contains convolve_channels function """
import numpy as np


def convolve_channels(images, kernel, padding='same', stride=(1, 1)):
    """ Function that performs a convolution with images with channels
    - images: numpy.ndarray with shape (m, h, w, c) containing multiple
    grayscale images
        m is the number of images
        h is the height in pixels of the images
        w is the width in pixels of the images
        c is the number of channels in the image
    - kernel: numpy.ndarray with shape (kh, kw, c) containing the kernel for
    the convolution
        kh is the height of the kernel
        kw is the width of the kernel
    - padding is either a tuple of (ph, pw), ‘same’, or ‘valid’
        if ‘same’, performs a same convolution
        if ‘valid’, performs a valid convolution
        if a tuple:
            ph is the padding for the height of the image
            pw is the padding for the width of the image
        the image should be padded with 0’s
    - stride: tuple of (sh, sw)
        sh is the stride for the height of the image
        sw is the stride for the width of the image
    """
    m, h, w, c = images.shape
    kh, kw, kc = kernel.shape
    sh, sw = stride
    if padding == 'same':
        p_h = ((((h - 1) * sh) + kh - h) // 2) + 1
        p_w = ((((w - 1) * sw) + kw - w) // 2) + 1
    elif padding == 'valid':
        p_h = 0
        p_w = 0
    elif type(padding) == tuple:
        p_h, p_w = padding

    W_out = ((w + (2 * p_w) - kw) // sw) + 1
    H_out = ((h + (2 * p_h) - kh) // sh) + 1
    p_images = np.pad(images, ((0, 0), (p_h, p_h), (p_w, p_w), (0, 0)),
                      'constant')
    output_matrix = np.zeros((m, H_out, W_out))
    for w in range(W_out):
        for h in range(H_out):
            part_image = p_images[:, sh*h:sh*h + kh, sw*w:sw*w + kw, :]
            output_matrix[:, h, w] = np.tensordot(part_image, kernel, axes=3)
    return output_matrix
