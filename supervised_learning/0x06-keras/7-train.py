#!/usr/bin/env python3
"""
module containing function train_model
"""
import tensorflow.keras as K


def train_model(network, data, labels, batch_size, epochs,
                validation_data=None,
                early_stopping=False, patience=0,
                learning_rate_decay=False, alpha=0.1, decay_rate=1,
                verbose=True, shuffle=False):
    """
    function that trains a model using mini-batch gradient descent,
        early stopping, learning rate decay and analyze validaiton data
    Args:
        network: model to train
        data: numpy.ndarray of shape (m, nx) containing the input data
        labels: one-hot numpy.ndarray of shape (m, classes)
            containing the labels of data
        batch_size: size of the batch used for mini-batch gradient descent
        epochs: number of passes through data for mini-batch gradient descent
        validation_data: data to validate the model with, if not None
        early_stopping: boolean that indicates whether early stopping
            should be used
        patience: patience used for early stopping
        learning_rate_decay: boolean that indicates whether learning rate decay
            should be used
        verbose: boolean that determines if output should be printed
            during training
        shuffle: boolean that determines whether to shuffle the batches
            every epoch
    Return: the History object generated after training the model
    """
    def learning_rate(epochs):
        """calculate learning rate"""
        return alpha / (1 + decay_rate * epochs)

    callback = []

    if early_stopping and validation_data:
        callback.append(K.callbacks.EarlyStopping(
            monitor='val_loss',
            patience=patience))

    if learning_rate_decay and validation_data:
        callback.append(K.callbacks.LearningRateScheduler(
            schedule=learning_rate,
            verbose=1))

    history = network.fit(
        data,
        labels,
        batch_size=batch_size,
        epochs=epochs,
        validation_data=validation_data,
        verbose=verbose,
        callbacks=[callback],
        shuffle=shuffle
    )

    return history
