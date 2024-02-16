#!/usr/bin/env python3
"""
module containing function gensim_to_keras
"""
from keras.layers import Embedding


def gensim_to_keras(model):
    """
    function that converts a gensim word2vec model to a keras Embedding layer
    Args:
        model: trained gensim word2vec models
    Return: the trainable keras Embedding
    """
    word_vectors = model.wv
    embedding_layer = word_vectors.get_keras_embedding(train_embeddings=True)

    return embedding_layer
