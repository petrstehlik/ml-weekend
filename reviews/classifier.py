#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# ML is a machine learning class for review classification.
#
# Copyright (C) 2017 Jiri Materna <jiri@mlguru.com>

import logging
import numpy as np
import nltk

from corpus import Corpus

from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn import metrics

from sklearn.dummy import DummyClassifier
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
        logger.info("Training the Baseline model.")
        self.baselineModel = Pipeline([('vec', CountVectorizer(tokenizer=self.tokenizer)),
                                      ('clf', DummyClassifier(strategy='stratified'))
                             ])
        self.baselineModel.fit(X, y)

    # Train a machine learning model using features X and targets y. If tfidf is true,
    # use the TF-IDF feature transformation. Store the trained model in self.model.
    def trainModel(self, X, y, model=SVC(kernel='linear'), tfidf=True):
        logger.info("Training the ML model. Data size={}.".format(len(X)))
        p = []

        p.append(('vec', CountVectorizer(tokenizer=self.tokenizer)))
        if tfidf: p.append(('tfidf', TfidfTransformer()))
        p.append(('clf', model))

        self.model = Pipeline(p)

        self.model.fit(X, y)

    # Predict targets for feature matrix data (features in columns) using the ML model.
    def predict(self, data):
        return self.model.predict(data)

    # Predict targets for feature matrix data (features in columns) using the baseline.
    def baselinePredict(self, data):
        return self.baselineModel.predict(data)

    # Evaluate the ML algorithm on the test data.
    # test_y - true target values
    # predicted_y - target values predicted using the ML algorithm
    # baseline_y - target values predicted using the baseline
    # names - class labels
    def evaluate(self, test_y, predicted_y, baseline_y, names):

        print ("BASELINE REPORT")
        print ("Accuracy: {}".format(metrics.accuracy_score(test_y, baseline_y)))
        print("Confusion matrix:")
        print(metrics.confusion_matrix(test_y, baseline_y))
        print(metrics.classification_report(test_y, baseline_y,
                                            target_names=names))
        print ("ML MODEL REPORT")
        print ("Accuracy: {}".format(metrics.accuracy_score(test_y, predicted_y)))
        print("Confusion matrix:")
        print(metrics.confusion_matrix(test_y, predicted_y))
        print(metrics.classification_report(test_y, predicted_y,
                                            target_names=names))


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
    #ml.trainModel(train_X, train_y, model=MultinomialNB(), tfidf=False)
    #ml.trainModel(train_X, train_y, model=LogisticRegression())
    ml.trainModel(train_X, train_y, model=SVC(kernel='linear'))
    #ml.trainModel(train_X, train_y, model=GradientBoostingClassifier(n_estimators=300))

    predicted_y = ml.predict(test_X)
    baseline_y = ml.baselinePredict(test_X)

    ml.evaluate(test_y, predicted_y, baseline_y, names)
