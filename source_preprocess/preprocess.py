import nltk
import string
import pandas as pd
import re


# Tokenizer function. You can add here different preprocesses.
def preprocess(sentence, labels):
    '''
    Task: Given a sentence apply all the required preprocessing steps
    to compute train our classifier, such as sentence splitting, 
    tokenization or sentence splitting.

    Input: Sentence in string format
    Output: Preprocessed sentence either as a list or a string
    '''
    # Place your code here
    # Keep in mind that sentence splitting affectes the number of sentences
    # and therefore, you should replicate labels to match.

    final_sentences = []
    final_labels = []

    for index,sent in sentence.items():
        s = sent.lower()
        sentence_p = s.translate(str.maketrans('', '', string.punctuation))

        final_sentences.append(sentence_p)
        final_labels.append(labels[index])

    return pd.Series(final_sentences),pd.Series(final_labels)


# Tokenizer function. You can add here different preprocesses.
def preprocess_char(sentence, labels):
    final_sentences = []
    final_labels = []

    for index, sent in sentence.items():
        s = sent.lower()
        l = nltk.tokenize.sent_tokenize(s)

        for i in l:
            sentence_p = i.translate(str.maketrans('', '', string.punctuation))
            final_sentences.append(sentence_p)
            final_labels.append(labels[index])

    return pd.Series(final_sentences), pd.Series(final_labels)

