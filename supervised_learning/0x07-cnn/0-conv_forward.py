#!/usr/bin/env python3
"""
module containing function conv_forward
"""
import numpy as np


def conv_forward(A_prev, W, b, activation, padding="same", stride=(1, 1)):
    """
    function that performs forward propagation over a convolutional layer
        of a neural network
    Args:
        A_prev: numpy.ndarray of shape (m, h_prev, w_prev, c_prev)
            containing the output of the previous layer
                m: number of examples
                h_prev: height of the previous layer
                w_prev: width of the previous layer
                c_prev: number of channels in the previous layer
        W: numpy.ndarray of shape (kh, kw, c_prev, c_new)
            containing the kernels for the convolution
                kh: filter height
                kw: filter width
                c_prev: number of channels in the previous layer
                c_new: number of channels in the output
        b: numpy.ndarray of shape (1, 1, 1, c_new)
            containing the biases applied to the convolution
        activation: activation function applied to the convolution
        padding: string that is either same or valid,
            indicating the type of padding used
        stride: tuple of (sh, sw) containing the strides for the convolution
            sh: stride for the height
            sw: stride for the width
    Return: output of the convolutional layer
    """
    m = A_prev.shape[0]
    h_prev = A_prev.shape[1]
    w_prev = A_prev.shape[2]
    c_prev = A_prev.shape[3]
    kh = W.shape[0]
    kw = W.shape[1]
    c_new = W.shape[3]
    sh = stride[0]
    sw = stride[1]

    # padding
    if padding == 'same':
        ph = int(((h_prev - 1) * sh + kh - h_prev) / 2)
        pw = int(((w_prev - 1) * sw + kw - w_prev) / 2)

    elif padding == 'valid':
        ph = 0
        pw = 0

    # convolved image shape
    convolved_image_h = int((h_prev + 2 * ph - kh) / sh) + 1
    convolved_image_w = int((w_prev + 2 * pw - kw) / sw) + 1

    # convolution with padding and stride
    convolved_images = np.zeros(
        shape=(m, convolved_image_h, convolved_image_w, c_new))

    pad_width = [(0, 0),
                 (ph, ph),
                 (pw, pw),
                 (0, 0)]
    padded_images = np.pad(A_prev,
                           pad_width,
                           mode='constant',
                           constant_values=0)

    for height in range(convolved_image_h):
        for width in range(convolved_image_w):
            for kernel in range(c_new):
                convolved_image = np.sum(np.multiply(
                    padded_images[:,
                                  height * sh:height * sh + kh,
                                  width * sw:width * sw + kw],
                    W[:, :, :, kernel]),
                    axis=(1, 2, 3))
                bias = b[:, :, :, kernel]
                convolved_images[:, height, width, kernel] = activation(
                    (convolved_image + bias))

    return convolved_images
