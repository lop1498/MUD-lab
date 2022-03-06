import nltk
import string
import pandas as pd

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
        print(sent)
        sentence_p = "".join([char for char in s if char not in string.punctuation])
        #words = nltk.wordpunct_tokenize(sentence_p)

        #porter = nltk.PorterStemmer()
        #stemmed = [porter.stem(word) for word in words]

        #final_sentences.append(stemmed)
        #final_labels.append([labels[index] for x in range(len(sent))])
        final_sentences.append(sentence_p)
        final_labels.append(labels[index])
        break

    final_sentences = [word for x in final_sentences for word in x]
    print(final_sentences)
    final_labels = [word for x in final_labels for word in x]

    return pd.Series(final_sentences),pd.Series(final_labels)


# Tokenizer function. You can add here different preprocesses.
def preprocess_char(sentence, labels):
    final_sentences = []
    final_labels = []

    for index, sent in sentence.items():
        s = sent.lower()
        sentence_p = "".join([char for char in s if char not in string.punctuation])

        final_sentences.append(sentence_p)
        final_labels.append(labels[index])

    return pd.Series(final_sentences), pd.Series(final_labels)

