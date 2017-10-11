#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# ML is a machine learning class for review classification.
#
# Copyright (C) 2017 Jiri Materna <jiri@mlguru.com>

import logging
import numpy as np

from corpus import Corpus

from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn import metrics

from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import GradientBoostingClassifier

logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
logging.root.setLevel(level=logging.INFO)
logger = logging.getLogger(__name__)

class ML:
    def __init__(self):
        self.model = None
        self.baselineModel = None

    # Split the input data into a list of tokens.
    def tokenizer(self, data):
        return nltk.tokenize.casual.casual_tokenize(data)

    # Fit a simple baseline model using features X and targets y.
    # Then store the model in self.baselineModel.
    def trainBaselineModel(self, X, y):
        #TODO

    # Train a machine learning model using features X and targets y. If tfidf is true,
    # use the TF-IDF feature transformation. Store the trained model in self.model.
    def trainModel(self, X, y, model=MultinomialNB(), tfidf=False):
        #TODO

    # Predict targets for feature matrix data (features in columns) using the ML model. 
    def predict(self, data):
        #TODO

    # Predict targets for feature matrix data (features in columns) using the baseline. 
    def baselinePredict(self, data):
        #TODO

    # Evaluate the ML algorithm on the test data.
    # test_y - true target values
    # predicted_y - target values predicted using the ML algorithm
    # baseline_y - target values predicted using the baseline
    # names - class labels
    def evaluate(self, test_y, predicted_y, baseline_y, names):
        #TODO

if __name__=='__main__':
    corpus = Corpus()
    corpus.loadData('../data/en_reviews.csv')
    #corpus.reduceClasses()    

    data = corpus.splitData(0.1)
    train_X = data['trainTexts']
    test_X = data['testTexts']
    train_y = np.array(data['trainTargets'])
    test_y = np.array(data['testTargets'])
    names = data['names']

    ml = ML()

    ml.trainBaselineModel(train_X, train_y)
    ml.trainModel(train_X, train_y, model=MultinomialNB(), tfidf=False)
    #ml.trainModel(train_X, train_y, model=LogisticRegression())
    #ml.trainModel(train_X, train_y, model=SVC(kernel='linear'))
    #ml.trainModel(train_X, train_y, model=GradientBoostingClassifier(n_estimators=300))
    
    predicted_y = ml.predict(test_X)
    baseline_y = ml.baselinePredict(test_X)
    
    ml.evaluate(test_y, predicted_y, baseline_y, names)
