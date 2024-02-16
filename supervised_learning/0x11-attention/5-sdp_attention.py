#!/usr/bin/env python3
"""
module containing function sdp_attention
"""
import tensorflow as tf


def sdp_attention(Q, K, V, mask=None):
    """
    function that calculates the scaled dot product attention
    Args:
        Q: tensor with its last two dimensions as (..., seq_len_q, dk)
            containing the query matrix
        K: tensor with its last two dimensions as (..., seq_len_v, dk)
            containing the key matrix
        V: tensor with its last two dimensions as (..., seq_len_v, dv)
            containing the value matrix
        mask: tensor that can be broadcast into (..., seq_len_q, seq_len_v)
            containing the optional mask, or defaulted to None
    Return: output, weights
        output: tensor with its last two dimensions as (..., seq_len_q, dv)
            containing the scaled dot product attention
        weights: tensor with its last two dimensions as
            (..., seq_len_q, seq_len_v) containing the attention weights
    """
    dk = tf.shape(Q)[-1]
    dk = tf.cast(dk, tf.float32)

    qk_t = tf.matmul(Q, K, transpose_b=True)
    scaled_matrix = qk_t / (tf.math.sqrt(dk))

    if mask is not None:
        scaled_matrix += mask * (-1e9)

    weights = tf.nn.softmax(scaled_matrix, axis=-1)

    output = tf.matmul(weights, V)

    return output, weights
