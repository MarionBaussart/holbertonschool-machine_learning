#!/usr/bin/env python3
"""
module containing class SelfAttention:
Class constructor: def __init__(self, units)
Public instance method:
    def call(self, s_prev, hidden_states)

"""
import tensorflow as tf


class SelfAttention(tf.keras.layers.Layer):
    """
    Class SelfAttention : inherits from tensorflow.keras.layers.Layer
         to calculate the attention for machine translation
    """

    def __init__(self, units):
        """
        Class contructor
        Args:
            units: integer representing the number of hidden units
                in the alignment model
        Public instance attributes:
            W: Dense layer with units units, to be applied to
                the previous decoder hidden state
            U: Dense layer with units units, to be applied to
                the encoder hidden states
            V: Dense layer with 1 units, to be applied to
                the tanh of the sum of the outputs of W and U
        """
        super().__init__()
        self.W = tf.keras.layers.Dense(units=units)
        self.U = tf.keras.layers.Dense(units=units)
        self.V = tf.keras.layers.Dense(units=1)

    def call(self, s_prev, hidden_states):
        """
        Public instance method corresponding to the self attention
        Args:
            s_prev: tensor of shape (batch, units)
                containing the previous decoder hidden state
            hidden_states: tensor of shape (batch, input_seq_len, units)
                containing the outputs of the encoder
        Returns: context, weights
            context: tensor of shape (batch, units)
                that contains the context vector for the decoder
            weights: tensor of shape (batch, input_seq_len, 1)
                that contains the attention weights
        """
        s_prev = tf.expand_dims(s_prev, axis=1)
        score = self.V(tf.nn.tanh(self.W(s_prev) + self.U(hidden_states)))

        weights = tf.nn.softmax(score, axis=1)

        context = weights * hidden_states
        context = tf.reduce_sum(context, axis=1)

        return context, weights
