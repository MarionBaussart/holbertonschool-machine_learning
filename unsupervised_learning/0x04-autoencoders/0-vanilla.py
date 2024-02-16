#!/usr/bin/env python3
"""
module containing function that create a vanilla autoencoder
"""
import tensorflow.keras as keras


def autoencoder(input_dims, hidden_layers, latent_dims):
    """
    function that creates a vanilla autoencoder
    Args:
        input_dims: integer containing the dimensions of the model input
        hidden_layers: list containing the number of nodes for each hidden
            layer in the encoder
        latent_dims: integer containing the dimensions of the latent space
            representation
    Return: encoder, decoder, auto
        encoder: the encoder model
        decoder: the decoder model
        auto: the full autoencoder model
    """
    inputs = keras.Input(shape=(input_dims,))

    # encoder model
    for i in range(len(hidden_layers)):
        if i == 0:
            encoded_output = keras.layers.Dense(
                hidden_layers[i],
                activation='relu'
            )(inputs)
        else:
            encoded_output = keras.layers.Dense(
                hidden_layers[i],
                activation='relu'
            )(encoded_output)
    encoded_output = keras.layers.Dense(
        latent_dims,
        activation='relu'
    )(encoded_output)

    encoder_model = keras.Model(inputs=inputs, outputs=encoded_output)

    # decoder model
    inputs = keras.Input(shape=(latent_dims,))
    for i in range(len(hidden_layers) - 1, -1, -1):
        if i == len(hidden_layers) - 1:
            decoded_output = keras.layers.Dense(
                hidden_layers[i],
                activation='relu'
            )(inputs)
        else:
            decoded_output = keras.layers.Dense(
                hidden_layers[i],
                activation='relu'
            )(decoded_output)
    decoded_output = keras.layers.Dense(
        input_dims,
        activation='sigmoid'
    )(decoded_output)

    decoder_model = keras.Model(inputs=inputs, outputs=decoded_output)

    # full autoencoder model
    inputs = keras.Input(shape=(input_dims,))
    autoencoder_model = keras.Model(
        inputs=inputs,
        outputs=decoder_model(encoder_model(inputs)))
    autoencoder_model.compile(optimizer='adam',
                              loss='binary_crossentropy')

    return encoder_model, decoder_model, autoencoder_model
