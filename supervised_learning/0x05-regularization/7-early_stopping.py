#!/usr/bin/env python3
"""
module containing function early_stopping
"""


def early_stopping(cost, opt_cost, threshold, patience, count):
    """
    function that determines if you should stop gradient descent early
    Args:
        cost: current validation cost of the neural network
        opt_cost: lowest recorded validation cost of the neural network
        threshold: threshold used for early stopping / threshold to whether
            quantify a loss at some epoch as improvement or not
        patience: patience count used for early stopping
        count: count of how long the threshold has not been met
    Return: a boolean of whether the network should be stopped early,
        followed by the updated count
    """
    early_stopping = False
    # If the difference of loss is below threshold,
    #   it is quantified as no improvement
    if opt_cost - cost <= threshold:
        count += 1
    else:
        count = 0
    if count >= patience:
        early_stopping = True
    return early_stopping, count
