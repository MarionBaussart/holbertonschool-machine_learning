#!/usr/bin/env python3
"""module containing class Neuron"""
import numpy as np


class Neuron:
    """
    Class Neuron : defines a single neuron performing binary classification
    """

    def __init__(self, nx):
        """
        Class contructor
        Args:
            nx: the number of input features to the neuron
        Private instance attributes:
            W: weights vector for the neuron
            b: bias for the neuron
            A: activated output of the neuron (prediction)
        """
        if type(nx) != int:
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")

        self.__W = np.random.randn(1, nx)
        self.__b = 0
        self.__A = 0

    @property
    def W(self):
        """
        getter function
        __W: weights vector for the neuron
        return private instance attribute __W
        """
        return self.__W

    @property
    def b(self):
        """
        getter function
        __b: bias for the neuron
        return private instance attribute __b
        """
        return self.__b

    @property
    def A(self):
        """
        getter function
        __A: activated output of the neuron (prediction)
        return private instance attribute __A
        """
        return self.__A
