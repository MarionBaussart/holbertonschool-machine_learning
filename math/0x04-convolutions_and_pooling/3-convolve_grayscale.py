#!/usr/bin/env python3
"""
module containing function convolve_grayscale
"""
import numpy as np


def convolve_grayscale(images, kernel, padding='same', stride=(1, 1)):
    """
    function that performs a convolution on grayscale images
        with custom padding and stride
    Args:
        images: numpy.ndarray with shape (m, h, w) containing multiple
            grayscale images
            m: number of images
            h: height in pixels of the images
            w: width in pixels of the images
        kernel: numpy.ndarray with shape (kh, kw) containing the kernel
            for the convolution
            kh: height of the kernel
            kw: width of the kernel
        padding: - tuple of (ph, pw)
            ph: padding for the height of the image
            pw: padding for the width of the image
                - same: performs a same convolution
                - valid: performs a valid convolution
        stride: tuple of (sh, sw)
            sh: stride for the height of the image
            sw: stride for the width of the image
    Return: a numpy.ndarray containing the convolved images
    """
    m = images.shape[0]
    h = images.shape[1]
    w = images.shape[2]
    kh = kernel.shape[0]
    kw = kernel.shape[1]
    sh = stride[0]
    sw = stride[1]

    # padding
    if padding == 'same':
        ph = int(((h - 1) * sh + kh - h) / 2) + 1
        pw = int(((w - 1) * sw + kw - w) / 2) + 1

    elif padding == 'valid':
        ph = 0
        pw = 0

    else:
        ph = padding[0]
        pw = padding[1]

    # convolved image shape
    convolved_image_h = ((h + 2 * ph - kh) / sh) + 1
    if int(convolved_image_h) > convolved_image_h:
        convolved_image_h = int(convolved_image_h) - 1
    else:
        convolved_image_h = int(convolved_image_h)

    convolved_image_w = ((w + 2 * pw - kw) / sw) + 1
    if int(convolved_image_w) > convolved_image_w:
        convolved_image_w = int(convolved_image_w) - 1
    else:
        convolved_image_w = int(convolved_image_w)

    # convolution with padding and stride
    convolved_images = np.zeros(
        shape=(m, convolved_image_h, convolved_image_w))

    pad_width = [(0, 0),
                 (ph, ph),
                 (pw, pw)]
    padded_images = np.pad(images,
                           pad_width,
                           mode='constant',
                           constant_values=0)

    for height in range(convolved_image_h):
        for width in range(convolved_image_w):
            convolved_image = np.sum(np.multiply(
                padded_images[:,
                              height * sh:height * sh + kh,
                              width * sw:width * sw + kw],
                kernel),
                axis=(1, 2))
            convolved_images[:, height, width] = convolved_image

    return convolved_images
