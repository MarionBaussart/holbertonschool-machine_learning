#!/usr/bin/env python3
"""
module containing class RNNEncoder:
Class constructor: def __init__(self, vocab, embedding, units, batch)
Public instance method:
    def initialize_hidden_state(self)
    def call(self, x, initial)

"""
import tensorflow as tf


class RNNEncoder(tf.keras.layers.Layer):
    """
    Class RNNEncoder : inherits from tensorflow.keras.layers.Layer
        to encode for machine translation
    """

    def __init__(self, vocab, embedding, units, batch):
        """
        Class contructor
        Args:
            vocab: integer representing the size of the input vocabulary
            embedding: integer representing the dimensionality of the embedding
                vector
            units: integer representing the number of hidden units
                in the RNN cell
            batch: integer representing the batch size
        Public instance attributes:
            batch: the batch size
            units: number of hidden units in the RNN cell
            embedding: keras Embedding layer that converts words from the
                vocabulary into an embedding vector
            gru: keras GRU layer with 'units' units
        """
        super().__init__()
        self.batch = batch
        self.units = units
        self.embedding = tf.keras.layers.Embedding(
            input_dim=vocab, output_dim=embedding)
        self.gru = tf.keras.layers.GRU(
            units=units,
            recurrent_initializer='glorot_uniform',
            return_sequences=True,
            return_state=True)

    def initialize_hidden_state(self):
        """
        Public instance method that initializes the hidden states
            for the RNN cell to a tensor of zeros
        Returns: a tensor of shape (batch, units)
            containing the initialized hidden states
        """
        shape = (self.batch, self.units)
        hidden_states_tensor = tf.zeros(shape=shape)

        return hidden_states_tensor

    def call(self, x, initial):
        """
        Public instance method corresponding to the encoder
        Args:
            x: tensor of shape (batch, input_seq_len) containing the input
                to the encoder layer as word indices within the vocabulary
            initial: tensor of shape (batch, units) containing the initial
                hidden state
        Returns: outputs, hidden
            outputs: tensor of shape (batch, input_seq_len, units)
                containing the outputs of the encoder
            hidden: tensor of shape (batch, units) containing the last hidden
                state of the encoder
        """
        embedding_vector = self.embedding(x)
        outputs, hidden = self.gru(inputs=embedding_vector,
                                   initial_state=initial)

        return outputs, hidden
