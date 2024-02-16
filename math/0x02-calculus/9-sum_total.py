#!/usr/bin/env python3trans
"""script that calculate the sum of i²"""


def summation_i_squared(n):
    """function that calculate the sum of i²
        Args:
            n is the stopping condition
        Return:
            the integer value of the sum, None if n is not a valid number
    """
    # using mathematics formule
    if type(n) == int and n >= 1:
        sum = (n * (n + 1) * ((2 * n) + 1)) / 6
        return int(sum)
    else:
        return None

    # with recursion:
    # if type(n) == int and n >= 1:
    #     if n == 1:
    #         return 1
    #     return int(summation_i_squared(n - 1) + n ** 2)
    # else:
    #     return None
