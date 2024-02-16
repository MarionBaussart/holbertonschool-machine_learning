#!/usr/bin/env python3
"""
module containing function positional_encoding
"""
import numpy as np


def positional_encoding(max_seq_len, dm):
    """
    function that calculates the positional encoding for a transformer
    Args:
        max_seq_len: integer representing the maximum sequence length
        dm: model depth
    Return: numpy.ndarray of shape (max_seq_len, dm)
        containing the positional encoding vectors
    """
    pe_matrix = np.zeros(shape=(max_seq_len, dm))

    for pos in range(max_seq_len):
        for i in np.arange(int(dm / 2)):
            denominator = np.power(10000, (2 * i) / dm)
            pe_matrix[pos, 2 * i] = np.sin(pos / denominator)
            pe_matrix[pos, (2 * i) + 1] = np.cos(pos / denominator)

    return pe_matrix
