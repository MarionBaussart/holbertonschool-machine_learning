#!/usr/bin/env python3
"""
module containing function that create a convolutional autoencoder
"""
import tensorflow.keras as keras


def autoencoder(input_dims, filters, latent_dims):
    """
    function that creates a convolutional autoencoder
    Args:
        input_dims: tuple of integers containing the dimensions of the model
            input
        filters: list containing the number of filters for each convolutional
            layer in the encoder
        latent_dims: tuple of integers containing the dimensions of the latent
            space representation
    Return: encoder, decoder, auto
        encoder: the encoder model
        decoder: the decoder model
        auto: the full autoencoder model
    """
    encoder_inputs = keras.Input(shape=input_dims)

    # encoder model
    for i in range(len(filters)):
        if i == 0:
            encoded_output = keras.layers.Conv2D(
                filters=filters[i],
                kernel_size=(3, 3),
                padding='same',
                activation='relu'
            )(encoder_inputs)
        else:
            encoded_output = keras.layers.Conv2D(
                filters=filters[i],
                kernel_size=(3, 3),
                padding='same',
                activation='relu'
            )(encoded_output)
        encoded_output = keras.layers.MaxPooling2D(
            pool_size=(2, 2)
        )(encoded_output)

    encoder_model = keras.Model(inputs=encoder_inputs, outputs=encoded_output)

    # decoder model
    decoder_inputs = keras.Input(shape=latent_dims)
    for i in range(len(filters) - 1, -1, -1):
        if i == len(filters) - 1:
            decoded_output = keras.layers.Conv2D(
                filters=filters[i],
                kernel_size=(3, 3),
                padding='same',
                activation='relu'
            )(decoder_inputs)
        elif i == 0:
            decoded_output = keras.layers.Conv2D(
                filters=filters[i],
                kernel_size=(3, 3),
                padding='valid',
                activation='relu'
            )(decoded_output)
        else:
            decoded_output = keras.layers.Conv2D(
                filters=filters[i],
                kernel_size=(3, 3),
                padding='same',
                activation='relu'
            )(decoded_output)
        decoded_output = keras.layers.UpSampling2D(
                size=(2, 2)
        )(decoded_output)

    decoded_output = keras.layers.Conv2D(
        filters=input_dims[-1],
        kernel_size=(3, 3),
        padding='same',
        activation='sigmoid'
    )(decoded_output)

    decoder_model = keras.Model(inputs=decoder_inputs, outputs=decoded_output)

    # full autoencoder model
    autoencoder_model = keras.Model(
        inputs=encoder_inputs,
        outputs=decoder_model(encoder_model(encoder_inputs)))
    autoencoder_model.compile(optimizer='adam',
                              loss='binary_crossentropy')

    return encoder_model, decoder_model, autoencoder_model
