# -*- coding: utf-8 -*-
#
# Corpus is a class for manipulation with a corpus of reviews.
#
# Copyright (C) 2017 Jiri Materna <jiri@mlguru.com>

import logging
import nltk
import csv

logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
logging.root.setLevel(level=logging.INFO)

class Corpus:
    def __init__(self):
        self.texts = []
        self.targets  = []
        self.names = ['Class 1', 'Class 2', 'Class 3','Class 4', 'Class 5']

    # Load data from a CSV file.
    def loadData(self, inFile):
        logging.info("Loading data from {}.".format(inFile))
        with open(inFile) as f:
            self.texts = []
            self.targets  = []
            fieldnames = ['rating', 'review']
            csvReader = csv.DictReader(f, fieldnames=fieldnames, delimiter='\t')
            for row in csvReader:
                rating = int(row['rating'])
                review = row['review']
                self.targets.append(rating)
                self.texts.append(review)

    # Reduce the number of classes by merging classes 1,2,3 and 4,5.
    def reduceClasses(self):
        self.targets = list(map(lambda t: 1 if t==4 or t==5 else 0, self.targets))
        self.names = ["Negative", "Positive"]

    # Split the data to test and train sets. 
    def splitData(self, testProportion=0.1):
        #we don't need to shuffle the data because it was shuffled before.
        testSize = int(len(self.targets)*testProportion)
        testTargets = self.targets[:testSize]
        testTexts = self.texts[:testSize]
        trainTargets = self.targets[testSize:]
        trainTexts = self.texts[testSize:]
        return {'testTexts': testTexts, 'testTargets': testTargets,
                'trainTexts': trainTexts, 'trainTargets': trainTargets,
                'names': self.names}
