#!/usr/bin/env python3trans
"""script that calculates the integral of a polynomial"""


def poly_integral(poly, C=0):
    """function that calculates the integral of a polynomial
        Args:
            poly is a list of coefficients representing a polynomial
            C is an integer representing the integration constant
        Return:
            a new list of coefficients representing the integral
            of the polynomial
    """
    if type(poly) != list or len(poly) == 0 or type(C) != int:
        return None

    if poly == [0]:
        return [C]

    integral = [C]
    for i in range(len(poly)):
        if (poly[i] / (i + 1)) % 1 == 0:
            integral.append(int(poly[i] / (i + 1)))
        else:
            integral.append(poly[i] / (i + 1))
    return integral
