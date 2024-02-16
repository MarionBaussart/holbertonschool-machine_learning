#!/usr/bin/env python3trans
"""script that calculates the derivative of a polynomial"""


def poly_derivative(poly):
    """function that calculates the derivative of a polynomial
        Args:
            poly is a list of coefficients representing a polynomial
        Return:
            a new list of coefficients representing the derivative
            of the polynomial
    """
    if type(poly) != list or len(poly) == 0:
        return None

    if len(poly) == 1:
        return [0]

    derivate = []
    for i in range(1, len(poly)):
        derivate.append(poly[i] * i)
    return derivate
