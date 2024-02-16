#!/usr/bin/env python3
"""
module containing function create_masks
"""
import tensorflow.compat.v2 as tf


def create_masks(inputs, target):
    """
    function that creates all masks for training/validation
    Args:
        inputs: tf.Tensor of shape (batch_size, seq_len_in)
            that contains the input sentence
        target: tf.Tensor of shape (batch_size, seq_len_out)
            that contains the target sentence
    Return: encoder_mask, combined_mask, decoder_mask
    """
    batch_size, seq_len_in = inputs.shape
    seq_len_out = target.shape[1]

    # Encoder mask
    encoder_mask = tf.cast(tf.math.equal(inputs, 0), dtype=tf.float32)
    encoder_mask = tf.reshape(encoder_mask,
                              shape=(batch_size, 1, 1, seq_len_in))

    # Combined mask
    look_ahead_mask = 1 - tf.linalg.band_part(
        tf.ones((seq_len_out, seq_len_out)), -1, 0)
    decoder_target_mask = tf.cast(tf.math.equal(target, 0), dtype=tf.float32)
    decoder_target_mask = tf.reshape(decoder_target_mask,
                                     shape=(batch_size, 1, 1, seq_len_out))

    combined_mask = tf.maximum(look_ahead_mask, decoder_target_mask)

    # Decoder mask
    decoder_mask = tf.cast(tf.math.equal(inputs, 0), dtype=tf.float32)
    decoder_mask = tf.reshape(decoder_mask,
                              shape=(batch_size, 1, 1, seq_len_in))

    return encoder_mask, combined_mask, decoder_mask
