#!/usr/bin/env python3
"""
module containing function conv_backward
"""
import numpy as np


def conv_backward(dZ, A_prev, W, b, padding="same", stride=(1, 1)):
    """
    function that performs back propagation over a convolutional layer
        of a neural network
    Args:
        dZ: numpy.ndarray of shape (m, h_new, w_new, c_new)
            containing the partial derivatives with respect to the unactivated
            output of the convolutional layer
                m: number of examples
                h_new: height of the output
                w_new: width of the output
                c_new: number of channels in the output
        A_prev: numpy.ndarray of shape (m, h_prev, w_prev, c_prev)
            containing the output of the previous layer
                h_prev: height of the previous layer
                w_prev: width of the previous layer
                c_prev: number of channels in the previous layer
        W: numpy.ndarray of shape (kh, kw, c_prev, c_new)
            containing the kernels for the convolution
                kh: filter height
                kw: filter width
        b: numpy.ndarray of shape (1, 1, 1, c_new)
            containing the biases applied to the convolution
        padding: string that is either same or valid,
            indicating the type of padding used
        stride: tuple of (sh, sw) containing the strides for the convolution
            sh: stride for the height
            sw: stride for the width
    Return: the partial derivatives with respect to the previous layer
        (dA_prev), the kernels (dW), and the biases (db)
    """
    m = dZ.shape[0]
    h_new = dZ.shape[1]
    w_new = dZ.shape[2]
    c_new = dZ.shape[3]
    h_prev = A_prev.shape[1]
    w_prev = A_prev.shape[2]
    c_prev = A_prev.shape[3]
    kh = W.shape[0]
    kw = W.shape[1]
    sh = stride[0]
    sw = stride[1]

    # padding
    if padding == 'same':
        ph = int(((h_prev - 1) * sh + kh - h_prev) / 2) + 1
        pw = int(((w_prev - 1) * sw + kw - w_prev) / 2) + 1

    elif padding == 'valid':
        ph = 0
        pw = 0

    # convolution with padding and stride
    pad_width = [(0, 0),
                 (ph, ph),
                 (pw, pw),
                 (0, 0)]
    padded_images = np.pad(A_prev,
                           pad_width,
                           mode='constant',
                           constant_values=0)

    # initialize dA_prev, dW and db
    dA_prev = np.zeros(shape=padded_images.shape)
    dW = np.zeros(shape=W.shape)
    db = np.sum(dZ, axis=(0, 1, 2), keepdims=True)

    for example in range(m):
        for height in range(h_new):
            for width in range(w_new):
                for kernel in range(c_new):
                    dA_prev[example,
                            height * sh:height * sh + kh,
                            width * sw:width * sw + kw,
                            :] += W[:, :, :, kernel] * dZ[example,
                                                          height,
                                                          width,
                                                          kernel]
                    dW[:, :, :, kernel] += padded_images[
                        example,
                        height * sh:height * sh + kh,
                        width * sw:width * sw + kw,
                        :
                        ] * dZ[example, height, width, kernel]

    # remove padding for dA
    if padding == "same":
        dA_prev = dA_prev[:, ph:-ph, pw:-pw, :]

    return dA_prev, dW, db
