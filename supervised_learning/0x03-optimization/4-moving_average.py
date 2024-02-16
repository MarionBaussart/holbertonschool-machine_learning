#!/usr/bin/env python3
"""
module containing function moving_average
"""


def moving_average(data, beta):
    """
    function that calculates the weighted moving average of a data set
    Args:
        data is: the list of data to calculate the moving average of
        beta: the weight used for the moving average
    Return: a list containing the moving averages of data
    v(t) = beta*v(t-1) + (1-beta)*data(t)
    bias correction = v / (1 - beta**(t))
    """
    data_moving_average = []
    v = 0
    for index in range(len(data)):
        v = (beta * v) + (1 - beta) * data[index]
        bias_correction = v / (1 - (beta ** (index + 1)))
        data_moving_average.append(bias_correction)

    return data_moving_average
