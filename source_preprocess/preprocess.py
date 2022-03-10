import nltk
import string
import pandas as pd
import re


def split_sentence(data):
    result = []
    for elem in data:
        result.append(elem.split("?"))
    return result


# Tokenizer function. You can add here different preprocesses.
def preprocess(sentence, labels):
    '''
    Task: Given a sentence apply all the required preprocessing steps
    to compute train our classifier, such as sentence splitting, 
    tokenization or sentence splitting.

    Input: Sentence in string format
    Output: Preprocessed sentence either as a list or a string
    '''

    final_sentences = []
    final_labels = []

    for index,sent in sentence.items():
        s = sent.lower()
        count = 0
        if '!' in s:
            count += 1

        if '?' in s:
            l = s.split('?')
            for l1 in l:
                sentence_p = l1.translate(str.maketrans('', '', string.punctuation))
                final_sentences.append(sentence_p)
                final_labels.append(labels[index])
        else:
            sentence_p = s.translate(str.maketrans('', '', string.punctuation))
            final_sentences.append(sentence_p)
            final_labels.append(labels[index])

    return pd.Series(final_sentences),pd.Series(final_labels)



