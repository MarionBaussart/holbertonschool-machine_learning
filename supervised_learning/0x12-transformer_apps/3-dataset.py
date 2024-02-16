#!/usr/bin/env python3
"""
module containing class Dataset:
Class constructor: def __init__(self)
Public instance method:
    def tokenize_dataset(self, data)
    def encode(self, pt, en)
    def tf_encode(self, pt, en)
"""
import tensorflow.compat.v2 as tf
import tensorflow_datasets as tfds


class Dataset:
    """
    Loads and preps a dataset for machine translation
    """

    def __init__(self, batch_size, max_len):
        """
        Class contructor
        Args:
            batch_size: batch size for training/validation
            max_len: maximum number of tokens allowed per example sentence
        Public instance attributes:
            data_train: contains the ted_hrlr_translate/pt_to_en
                tf.data.Dataset train split, loaded as_supervided
            data_valid: contains the ted_hrlr_translate/pt_to_en
                tf.data.Dataset validate split, loaded as_supervided
            tokenizer_pt: Portuguese tokenizer created from the training set
            tokenizer_en: English tokenizer created from the training set
        """
        examples, metadata = tfds.load('ted_hrlr_translate/pt_to_en',
                                       with_info=True,
                                       as_supervised=True)
        self.data_train = examples['train']
        self.data_valid = examples['validation']

        self.tokenizer_pt, self.tokenizer_en = self.tokenize_dataset(
            self.data_train)

        self.data_train = self.data_train.map(self.tf_encode)
        self.data_valid = self.data_valid.map(self.tf_encode)

        # filter out all examples
        def filter_func(x, y, max_len=max_len):
            """
            Filter out all examples that have either sentence
            with more than max_len tokens
            """
            filtered = tf.logical_and(tf.size(x) <= max_len,
                                      tf.size(y) <= max_len)
            return filtered

        self.data_train = self.data_train.filter(filter_func)
        self.data_valid = self.data_valid.filter(filter_func)

        # cache the dataset to increase performance
        self.data_train = self.data_train.cache()

        # shuffle the entire dataset
        self.data_train = self.data_train.shuffle(
            metadata.splits['train'].num_examples)

        # split the dataset into padded batches
        self.data_train = self.data_train.padded_batch(batch_size)
        self.data_valid = self.data_valid.padded_batch(batch_size)

        # prefetch the dataset
        self.data_train = self.data_train.prefetch(
            tf.data.experimental.AUTOTUNE)

    def tokenize_dataset(self, data):
        """
        Public instance method that creates sub-word tokenizers for our dataset
        Args:
            data: tf.data.Dataset whose examples are formatted as a tuple
                (pt, en)
        Returns: tokenizer_pt, tokenizer_en
            Portuguese tokenizer and English tokenizer
        """
        SubwordTextEncoder = tfds.deprecated.text.SubwordTextEncoder
        tokenizer_pt = SubwordTextEncoder.build_from_corpus(
            (pt.numpy() for pt, en in data), target_vocab_size=2**15)
        tokenizer_en = SubwordTextEncoder.build_from_corpus(
            (en.numpy() for pt, en in data), target_vocab_size=2**15)

        return tokenizer_pt, tokenizer_en

    def encode(self, pt, en):
        """
        Public instance method that encodes a translation into tokens
        Args:
            pt: tf.Tensor containing the Portuguese sentence
            en: tf.Tensor containing the corresponding English sentence
        Returns: pt_tokens, en_tokens
            pt_tokens: np.ndarray containing the Portuguese tokens
            en_tokens: np.ndarray containing the English tokens
        """
        pt_tokens = [self.tokenizer_pt.vocab_size] + self.tokenizer_pt.encode(
            pt.numpy()) + [self.tokenizer_pt.vocab_size + 1]
        en_tokens = [self.tokenizer_en.vocab_size] + self.tokenizer_en.encode(
            en.numpy()) + [self.tokenizer_en.vocab_size + 1]

        return pt_tokens, en_tokens

    def tf_encode(self, pt, en):
        """
        Public instance method that acts as a tensorflow wrapper for the encode
        instance method
        Args:
            pt: tf.Tensor containing the Portuguese sentence
            en: tf.Tensor containing the corresponding English sentence
        Returns: pt_tokens, en_tokens
            pt_tokens: np.ndarray containing the Portuguese tokens
            en_tokens: np.ndarray containing the English tokens
        """
        pt_tensor, en_tensor = tf.py_function(func=self.encode,
                                              inp=[pt, en],
                                              Tout=[tf.int64, tf.int64])
        pt_tensor.set_shape([None])
        en_tensor.set_shape([None])

        return pt_tensor, en_tensor
