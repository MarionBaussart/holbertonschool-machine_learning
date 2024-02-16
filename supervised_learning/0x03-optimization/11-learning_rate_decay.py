#!/usr/bin/env python3
"""
module containing function learning_rate_decay
"""


def learning_rate_decay(alpha, decay_rate, global_step, decay_step):
    """
    function that updates the learning rate using inverse time decay in numpy
    Args:
        alpha: the original learning rate
        decay_rate: the weight used to determine the rate
            at which alpha will decay
        global_step: the number of passes of gradient descent that have elapsed
        decay_step: the number of passes of gradient descent that should occur
            before alpha is decayed further
    Return: the updated value for alpha
    """
    updated_alpha = alpha / (1 + decay_rate * (int(global_step / decay_step)))

    return updated_alpha
