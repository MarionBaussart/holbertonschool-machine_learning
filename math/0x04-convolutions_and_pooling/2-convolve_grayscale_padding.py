#!/usr/bin/env python3
"""
module containing function convolve_grayscale_padding
"""
import numpy as np


def convolve_grayscale_padding(images, kernel, padding):
    """
    function that performs a convolution on grayscale images
        with custom padding
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
        padding: tuple of (ph, pw)
            ph: padding for the height of the image
            pw: padding for the width of the image
    Return: a numpy.ndarray containing the convolved images
    """
    m = images.shape[0]
    h = images.shape[1]
    w = images.shape[2]
    kh = kernel.shape[0]
    kw = kernel.shape[1]
    ph = padding[0]
    pw = padding[1]

    convolved_image_h = h + 2 * ph - kh + 1
    convolved_image_w = w + 2 * pw - kw + 1

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
                padded_images[:, height:height + kh, width:width + kw],
                kernel),
                axis=(1, 2))
            convolved_images[:, height, width] = convolved_image

    return convolved_images
