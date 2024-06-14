import nltk
import numpy as np
from nltk.stem import *

stemmer = WordNetLemmatizer()

def tokenization(sentence):
    return nltk.word_tokenize(sentence)

def stemming(word):
    return stemmer.lemmatize(word.lower())

# print(tokenization("What the hell is up wiht you"))
# print(stemming("organs"))

def bag_of_words(tokenized_sentence, all_words):
    sentence_words = [stemming(word) for word in tokenized_sentence]
    # initialize bag with 0 for each word
    bag = np.zeros(len(all_words), dtype=np.float32)
    for idx, w in enumerate(all_words):
        if w in sentence_words: 
            bag[idx] = 1

    return bag

# sentence = ["hello", "how", "are", "you"]
# words = ["hi", "hello", "I", "you", "bye", "thank", "cool"]
# print(bag_of_words(sentence, words))