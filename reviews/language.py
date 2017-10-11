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

    # Create an n-gram model from the trainCorpus and store it to the modelPath directory.
    def createModel(self, trainCorpus):
        #TODO

    # Load the n-gram model from the modelPath directory.
    def loadModel(self):
        #TODO
    
    # Get the probability of bigram. Use the Laplace smooting.
    def getProbability(self, bigram):
        #TODO

    # Get the perplexity of normalizedText.
    def getPerplexity(self, normalizedText):
        #TODO

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

    print(detector.detectLang('This is an example of the english language.', #TODO))
    print(detector.detectLang('Another text written in the target language which should pass.', #TODO))
    print(detector.detectLang('Toto je ukázkový český text.', #TODO))
    print(detector.detectLang('Následuje alternativní posloupnost znaků.', #TODO))
