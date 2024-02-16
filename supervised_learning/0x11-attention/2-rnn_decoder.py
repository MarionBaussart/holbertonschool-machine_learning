#!/usr/bin/env python3
"""
module containing class RNNDecoder:
Class constructor: def __init__(self, vocab, embedding, units, batch)
Public instance method:
    def call(self, x, s_prev, hidden_states)

"""
import tensorflow as tf
SelfAttention = __import__('1-self_attention').SelfAttention


class RNNDecoder(tf.keras.layers.Layer):
    """
    Class RNNDecoder : inherits from tensorflow.keras.layers.Layer
         to decode for machine translation
    """

    def __init__(self, vocab, embedding, units, batch):
        """
        Class contructor
        Args:
            vocab: integer representing the size of the output vocabulary
            embedding: integer representing the dimensionality of the embedding
                vector
            units: integer representing the number of hidden units in the RNN
                cell
            batch: integer representing the batch size
        Public instance attributes:
            embedding: keras Embedding layer that converts words from the
                vocabulary into an embedding vector
            gru: keras GRU layer with 'units' units
            F: Dense layer with vocab units
        """
        super().__init__()
        self.batch = batch
        self.embedding = tf.keras.layers.Embedding(
            input_dim=vocab, output_dim=embedding)
        self.gru = tf.keras.layers.GRU(
            units=units,
            recurrent_initializer='glorot_uniform',
            return_sequences=True,
            return_state=True)
        self.F = tf.keras.layers.Dense(units=vocab)

    def call(self, x, s_prev, hidden_states):
        """
        Public instance method corresponding to the RNN decoder
        Args:
            x: tensor of shape (batch, 1)
                containing the previous word in the target sequence as an index
                of the target vocabulary
            s_prev: tensor of shape (batch, units)
                containing the previous decoder hidden state
            hidden_states: tensor of shape (batch, input_seq_len, units)
                containing the outputs of the encoder
        Returns: y, s
            y: tensor of shape (batch, vocab)
                containing the output word as a one hot vector in the target
                vocabulary
            hidden: tensor of shape (batch, units)
                containing the new decoder hidden state
        """
        units = s_prev.shape[1]
        self_attention = SelfAttention(units)
        context, _ = self_attention(s_prev, hidden_states)
        embedding_vector = self.embedding(x)
        context = tf.expand_dims(context, axis=1)
        inputs = tf.concat((context, embedding_vector), axis=-1)
        outputs, hidden = self.gru(inputs=inputs)

        outputs = tf.reshape(outputs, shape=(outputs.shape[0],
                                             outputs.shape[2]))
        y = self.F(outputs)

        return y, hidden
