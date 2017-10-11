#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Read reviews from a CSV file and filter out all non-English items. 
#
# Copyright (C) 2017 Jiri Materna <jiri@mlguru.com>

import csv
import sys
import logging
import argparse
from language import Detector

logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
logging.root.setLevel(level=logging.INFO)
logger = logging.getLogger(__name__)

parser = argparse.ArgumentParser("Filter all non-english reviews.")
parser.add_argument('--fin', type=str, default='../data/reviews.csv',
                   help='Path to the input csv file.')
parser.add_argument('--fout', type=str, default='../data/en_reviews.csv',
                   help='Path to the output csv file.')

args = parser.parse_args()
INPUT_FILE = args.fin
OUTPUT_FILE = args.fout

ld = Detector('../data/language_model/')
ld.loadModel()

counter = 0
with open(INPUT_FILE) as inFile:
    with open(OUTPUT_FILE, "w") as outFile:
        fieldnames = ['rating', 'review']
        csvReader = csv.DictReader(inFile, fieldnames=fieldnames, delimiter='\t')
        csvWriter = csv.DictWriter(outFile, fieldnames=fieldnames, delimiter='\t')
        for row in csvReader:
            review = row['review']
            if (ld.detectLang(review, #TODO)):
                csvWriter.writerow(row)
                counter += 1
logger.info("{} english reviews written.".format(counter))
