import nltk
import string

#Tokenizer function. You can add here different preprocesses.
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

    for i in range(len(sentence)):
        s = sentence[i].lower()
        sentence_p = "".join([char for char in s if char not in string.punctuation])
        words = nltk.word_tokenize(sentence_p)

        porter = nltk.PorterStemmer()
        stemmed = [porter.stem(word) for word in words]

        final_sentences.append(stemmed)
        final_labels.append([labels[i] for x in range(len(sentence[i]))])

    return sentence,labels



