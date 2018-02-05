#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# The Detector class creates an n-gram language model and is able to detect
# whether an unseen text is in the same langueage as the training text.
# 
# Copyright (C) 2017 Jiri Materna <jiri@mlguru.com>

import os
import logging
import pickle
import math
import re
import numpy as np
from gensim.corpora.wikicorpus import filter_wiki, tokenize

logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
logging.root.setLevel(level=logging.INFO)
logger = logging.getLogger(__name__)

class Detector:
    # Constructor of the Detector class. modelPath is a directory for storing the n-gram model.
    def __init__(self, modelPath):
        #TODO
        self.modelPath = os.path.join(modelPath, 'ngram.pkl')

    # Create an n-gram model from the trainCorpus and store it to the modelPath directory.
    def createModel(self, trainCorpus):
        print("creating model")
        with open(trainCorpus) as f:
            self.model = f.read().split(' ')
            self.ngrams = list()

            for i in range(len(self.model) - 1):
                self.ngrams.append(self.model[i:i+2])
                self.dict_size = len(self.model)

            with open(self.modelPath, 'wb+') as mp:
                print("dumping model")
                pickle.dump({'ngrams' : self.ngrams, 'dict_size' : self.dict_size, 'model' : self.model}, mp)


    # Load the n-gram model from the modelPath directory.
    def loadModel(self):
        print("loading model")
        with open(self.modelPath, 'rb') as mp:
            p = pickle.load(mp)
            self.dict_size = p['dict_size']
            self.ngrams = p['ngrams']
            self.model = p['model']

    # Get the probability of bigram. Use the Laplace smooting.
    def getProbability(self, bigram):
        #TODO
        count_bigram = self.ngrams.count(bigram) + 1
        count_unigram = self.model.count(bigram[0]) + self.dict_size

        print(count_bigram)
        print(count_unigram)

        return(count_bigram / count_unigram)

    # Get the perplexity of normalizedText.
    def getPerplexity(self, normalizedText):
        #TODO
        self.text = normalizedText.split(' ')

        ngrams = list()
        for i in range(len(self.text) - 1):
            ngrams.append(self.text[i:i+2])

        prob = 0.0

        for ngram in ngrams:
            prob += math.log2(self.getProbability(ngram))

        print(2**(-(prob/self.dict_size)))

        return(2**(-(prob/self.dict_size)))

    # Transform text to a normalized form where all tokens are separated with spaces.
    def normalizeText(self, text):
        words = tokenize(filter_wiki(text.lower()))
        text = " ".join(words)
        return text

    # Detect the language of text using threshold. Return 1 if the text is long enough and is 
    # written in the target language,else return 0.
    def detectLang(self, text, threshold):
        #normalize the text and remove all specials
        text = self.normalizeText(text)
        if len(text) <= 1:
            return 0
        else:
            return 1 if self.getPerplexity(text) <= threshold else 0

    def __find_ngrams(self, input_list, n):
        return zip(*[input_list[i:] for i in range(n)])

THRESHOLD = 0.5

if __name__=='__main__':
    detector = Detector('../data/language_model/')
    #detector.createModel('../data/corpora/enlang1.txt')
    detector.loadModel()
    print(detector.detectLang('This is an example of the english language.', THRESHOLD))
    print(detector.detectLang('Another text written in the target language which should pass.', THRESHOLD))
    print(detector.detectLang('Toto je ukázkový český text.', THRESHOLD))
    print(detector.detectLang('Následuje alternativní posloupnost znaků.', THRESHOLD))

