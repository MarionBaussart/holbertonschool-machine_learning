#!/usr/bin/env python3
"""
python script that trains a convolutional neural network
to classify the CIFAR 10 dataset
"""
import tensorflow.keras as K

# Preprocessing the data
def preprocess_data(X, Y):
    """
    function that prepocess the data
    Args:
        X: numpy.ndarray of shape (m, 32, 32, 3) containing the CIFAR 10 data,
            where m is the number of data points
        Y: numpy.ndarray of shape (m,) containing the CIFAR 10 labels for X
    Return: X_p, Y_p, numpy.ndarray containing the preprocessed X and Y
    """
    X_p = K.applications.xception.preprocess_input(X)
    Y_p = K.utils.to_categorical(Y,
                                 num_classes=10,                          dtype='float32')
    return X_p, Y_p

# trains a convolutional neural network to classify the CIFAR 10 dataset
if __name__ == '__main__':

    # load data
    (X_train, Y_train), (X_test, Y_test) = K.datasets.cifar10.load_data()
    X_train, Y_train = preprocess_data(X_train, Y_train)
    X_test, Y_test = preprocess_data(X_test, Y_test)

    Xception_model = K.applications.Xception(
        include_top=False,
        weights="imagenet",
        input_shape=(288, 288, 3))

    # freeze the pretrained model
    Xception_model.trainable = False

    # keep a copy of the weights of frozen layers
    Xception_weights_values = Xception_model.get_weights()

    # scale up the input data
    inputs = K.Input(shape=(32, 32, 3))
    inputs_resized = K.layers.Lambda(
        lambda image: K.backend.resize_images(
            image,
            height_factor=288 // 32,
            width_factor=288 // 32,
            data_format="channels_last",
            interpolation="bilinear"))(inputs)

    # build the model
    output = Xception_model(inputs_resized, training=False)
    output = K.layers.Flatten()(output)
    output = K.layers.Dense(10, activation="softmax")(output)

    # train the model
    model = K.Model(inputs=inputs, outputs=output)

    optimizer = K.optimizers.Adam(learning_rate=0.001,
                                beta_1=0.99,
                                beta_2=0.9,
                                name='Adam')
    model.compile(optimizer=optimizer,
                    loss='categorical_crossentropy',
                    metrics=['accuracy'])

    # early stopping
    callback = []
    callback.append(K.callbacks.EarlyStopping(
        monitor='val_loss',
        patience=3))

    # save only best model
    callback.append(K.callbacks.ModelCheckpoint(
        filepath="cifar10.h5",
        monitor='val_loss',
        save_best_only=True,
        save_freq="epoch"
    ))

    model.fit(
        X_train,
        Y_train,
        batch_size=128,
        epochs=5,
        validation_data=(X_test, Y_test),
        verbose=True,
        callbacks=[callback],
        shuffle=False
    )

    # save the training model
    model.save("cifar10.h5")
