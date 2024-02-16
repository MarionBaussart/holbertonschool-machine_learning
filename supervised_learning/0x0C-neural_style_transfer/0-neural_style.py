#!/usr/bin/env python3
"""
module containing class NST:
Public class attributes:
    style_layers, content_layer
Class constructor:
    def __init__(self, style_image, content_image, alpha=1e4, beta=1)
Public instance attributes:
    style_image, content_image, alpha, beta
Static Method:
    def scale_image(image)
"""
import numpy as np
import tensorflow as tf


class NST:
    """
    Class NST : performs tasks for neural style transfer
    """

    style_layers = ['block1_conv1',
                    'block2_conv1',
                    'block3_conv1',
                    'block4_conv1',
                    'block5_conv1']
    content_layer = 'block5_conv2'

    def __init__(self, style_image, content_image, alpha=1e4, beta=1):
        """
        Class contructor
        Args:
            style_image: image used as a style reference,
                stored as a numpy.ndarray
            content_image: image used as a content reference,
                stored as a numpy.ndarray
            alpha: weight for content cost
            beta: weight for style cost
        """
        if type(style_image) != np.ndarray or len(style_image.shape) != 3 or \
           style_image.shape[2] != 3:
            raise TypeError(
                'style_image must be a numpy.ndarray with shape (h, w, 3)')

        if type(content_image) != np.ndarray or len(content_image.shape) != 3 \
           or content_image.shape[2] != 3:
            raise TypeError(
                'content_image must be a numpy.ndarray with shape (h, w, 3)')

        if (type(alpha) != int and type(alpha) != float) or alpha < 0:
            raise TypeError('alpha must be a non-negative number')

        if (type(beta) != int and type(beta) != float) or beta < 0:
            raise TypeError('beta must be a non-negative number')

        tf.compat.v1.enable_eager_execution(
            config=None, device_policy=None, execution_mode=None)

        self.style_image = self.scale_image(style_image)
        self.content_image = self.scale_image(content_image)
        self.alpha = alpha
        self.beta = beta

    @staticmethod
    def scale_image(image):
        """
        Static method that rescales an image
            such that its pixels values are between 0 and 1
            and its largest side is 512 pixels
        Args:
            image: numpy.ndarray of shape (h, w, 3)
                containing the image to be scaled
        """
        if type(image) != np.ndarray or len(image.shape) != 3 \
           or image.shape[2] != 3:
            raise TypeError(
                'image must be a numpy.ndarray with shape (h, w, 3)')

        resized_image = tf.image.resize(images=image,
                                        size=[512, 512],
                                        preserve_aspect_ratio=True,
                                        method='bicubic')

        scaled_image = resized_image / 255
        scaled_image = tf.clip_by_value(scaled_image,
                                        clip_value_min=0,
                                        clip_value_max=1)

        scaled_image = tf.expand_dims(scaled_image, axis=0)

        return scaled_image
