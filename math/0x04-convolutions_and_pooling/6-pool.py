#!/usr/bin/env python3
"""
module containing function pool
"""
import numpy as np


def pool(images, kernel_shape, stride, mode='max'):
    """
    function that performs pooling on images
    Args:
        images: numpy.ndarray with shape (m, h, w, c) containing multiple
            grayscale images
            m: number of images
            h: height in pixels of the images
            w: width in pixels of the images
            c: number of channels in the image
        kernel_shape: numpy.ndarray with shape (kh, kw) containing the kernel
            for the convolution
            kh: height of the kernel
            kw: width of the kernel
        stride: tuple of (sh, sw)
            sh: stride for the height of the image
            sw: stride for the width of the image
        mode: indicates the type of pooling
            max: indicates max pooling
            avg: indicates average pooling
    Return: a numpy.ndarray containing the pooled images
    """
    m = images.shape[0]
    h = images.shape[1]
    w = images.shape[2]
    c = images.shape[3]
    kh = kernel_shape[0]
    kw = kernel_shape[1]
    sh = stride[0]
    sw = stride[1]

    # convolved image shape
    convolved_image_h = ((h - kh) / sh) + 1
    if int(convolved_image_h) > convolved_image_h:
        convolved_image_h = int(convolved_image_h) - 1
    else:
        convolved_image_h = int(convolved_image_h)

    convolved_image_w = ((w - kw) / sw) + 1
    if int(convolved_image_w) > convolved_image_w:
        convolved_image_w = int(convolved_image_w) - 1
    else:
        convolved_image_w = int(convolved_image_w)

    # convolution with padding and stride
    convolved_images = np.zeros(
        shape=(m, convolved_image_h, convolved_image_w, c))

    for height in range(convolved_image_h):
        for width in range(convolved_image_w):
            if mode == 'max':
                convolved_image = np.nanmax(
                    images[:,
                           height * sh:height * sh + kh,
                           width * sw:width * sw + kw],
                    axis=(1, 2))
                convolved_images[:, height, width] = convolved_image
            if mode == 'avg':
                convolved_image = np.nanmean(
                    images[:,
                           height * sh:height * sh + kh,
                           width * sw:width * sw + kw],
                    axis=(1, 2))
                convolved_images[:, height, width] = convolved_image

    return convolved_images
