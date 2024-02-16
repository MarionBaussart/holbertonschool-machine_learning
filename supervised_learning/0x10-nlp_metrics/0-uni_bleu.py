#!/usr/bin/env python3
"""
module containing function uni_bleu
"""


def uni_bleu(references, sentence):
    """
    function that calculates the unigram BLEU score for a sentence
    Args:
        references: list of reference translations
            each reference translation: list of the words in the translation
        sentence: list containing the model proposed sentence
    Return: unigram BLEU score
    """
    bleu_unigram = 0

    nb_predicted_word = len(sentence)
    print("nb_predicted_word:", nb_predicted_word)

    predicted_word = {}
    for word in sentence:
        predicted_word[word] = sentence.count(word)

    print("predicted_word:", predicted_word)

    references_word = {}
    for ref_sentence in references:
        for word in ref_sentence:
            if word in predicted_word:
                references_word[word] = ref_sentence.count(word)

    for ref_sentence in references:
        for word in ref_sentence:
            if word in predicted_word:
                references_word[word] = max(ref_sentence.count(word), references_word[word])
    print("references_word:", references_word)

    nb_correct_predicted_word = 0
    for key in references_word:
        if references_word[key] > predicted_word[key]:
            nb_correct_predicted_word += predicted_word[key]
        else:
            nb_correct_predicted_word += references_word[key]

    precision = nb_correct_predicted_word / nb_predicted_word
    print("precision:", precision)



    return bleu_unigram