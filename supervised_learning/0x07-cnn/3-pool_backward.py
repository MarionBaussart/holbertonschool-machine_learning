#!/usr/bin/env python3
"""
module containing function pool_backward
"""
import numpy as np


def pool_backward(dA, A_prev, kernel_shape, stride=(1, 1), mode='max'):
    """
    function that performs back propagation over a pooling layer
        of a neural network
    Args:
        dA: numpy.ndarray of shape (m, h_new, w_new, c)
            containing the partial derivatives with respect to
            the output of the pooling layer
                m: number of examples
                h_new: height of the output
                w_new: width of the output
                c: number of channels
        A_prev: numpy.ndarray of shape (m, h_prev, w_prev, c)
            containing the output of the previous layer
                h_prev: height of the previous layer
                w_prev: width of the previous layer
        kernel_shape: tuple of (kh, kw) containing the size of the kernel
            for the pooling
                kh: filter height
                kw: filter width
        stride: tuple of (sh, sw) containing the strides for the pooling
            sh: stride for the height
            sw: stride for the width
        mode: string containing either max or avg,
            indicating whether to perform maximum or average pooling
    Return: partial derivatives with respect to the previous layer (dA_prev)
    """
    m = dA.shape[0]
    h_new = dA.shape[1]
    w_new = dA.shape[2]
    c = dA.shape[3]
    h_prev = A_prev.shape[1]
    w_prev = A_prev.shape[2]
    kh = kernel_shape[0]
    kw = kernel_shape[1]
    sh = stride[0]
    sw = stride[1]

    dA_prev = np.zeros(A_prev.shape)

    for example in range(m):
        for height in range(h_new):
            for width in range(w_new):
                for channel in range(c):
                    if mode == 'max':
                        mask = (A_prev[
                            example,
                            height * sh:height * sh + kh,
                            width * sw:width * sw + kw,
                            channel] == np.max(A_prev[
                                example,
                                height * sh:height * sh + kh,
                                width * sw:width * sw + kw,
                                channel]))
                        dA_prev[
                            example,
                            height * sh:height * sh + kh,
                            width * sw:width * sw + kw,
                            channel] += mask * dA[
                                example,
                                height,
                                width,
                                channel]
                    if mode == 'avg':
                        average_dA = dA[
                            example,
                            height,
                            width,
                            channel] / (kh * kw)
                        dA_prev[
                            example,
                            height * sh:height * sh + kh,
                            width * sw:width * sw + kw,
                            channel] += np.ones((kh, kw)) * average_dA

    return dA_prev
