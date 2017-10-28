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
        self.modelPath = modelPath
        if not os.path.exists(modelPath):
            os.makedirs(modelPath)
        self.V = None
        self.histogram = None

    # Create an n-gram model from the trainCorpus and store it to the modelPath directory.
    def createModel(self, trainCorpus):
        self.histogram = {}
        with open(self.modelPath + '/model.pkl', 'wb') as fout:
            logger.info("Generating histogram of unigrams and bigrams from {}".format(trainCorpus))
            with open(trainCorpus) as fin:
                for doc in fin.readlines():
                    for i in range(len(doc)-2):
                        bigram = doc[i:i+2]
                        unigram = doc[i]
                        self.histogram[bigram] = self.histogram.get(bigram, 0) + 1
                        self.histogram[unigram] = self.histogram.get(unigram, 0) + 1
                self.V = len([unigram for unigram in self.histogram.keys() if len(unigram) == 1])
            pickle.dump((self.histogram, self.V), fout)

    # Load the n-gram model from the modelPath directory.
    def loadModel(self):
        with open(self.modelPath + '/model.pkl', 'rb') as fin:
            (self.histogram, self.V) = pickle.load(fin)
        logger.info("Language model successfully loaded from {}.".format(self.modelPath + '/model.pkl'))
    
    # Get the probability of bigram. Use the Laplace smooting.
    def getProbability(self, bigram):
        #use the Laplace smoothing
        return 1.0*(self.histogram.get(bigram, 0) + 1) / \
                   (self.histogram.get(bigram[0], 0) + self.V)

    # Get the perplexity of normalizedText.
    def getPerplexity(self, normalizedText):
        bigrams = [normalizedText[i:i+2] for i in range(len(normalizedText) - 1)]
        h = -sum(map(lambda x: np.log2(self.getProbability(x)), bigrams))
        return np.power(2, h/len(bigrams))

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

if __name__=='__main__':
    detector = Detector('../data/language_model/')

    detector.createModel('../data/corpora/enlang1.txt')

    print(detector.detectLang('This is an example of the english language.', 14))
    print(detector.detectLang('Another text written in the target language which should pass.', 14))
    print(detector.detectLang('Toto je ukázkový český text.', 14))
    print(detector.detectLang('Následuje alternativní posloupnost znaků.', 14))
