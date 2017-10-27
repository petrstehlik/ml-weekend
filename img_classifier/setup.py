#!/usr/bin/env python

import logging
import os
import subprocess
import sys

logging.basicConfig(level=logging.INFO, stream=sys.stdout)

PATH_TO_PACKAGE = "ml-weekend/img_classifier/"

os.environ["AIRCRAFT_DATA"] = 'data/fgvc-aircraft-2013b/data'

DATA_URL = "https://storage.googleapis.com/airliners/fgvc-aircraft-2013b.zip"

logging.info("Running installation...")
subprocess.call(["mkdir", "data"])
subprocess.call(["mkdir", "notebooks"])

logging.info("Folders created")
logging.info("Downloading dataset...")
subprocess.call(["wget", DATA_URL])

logging.info("..done")
logging.info("Unpacking archive to data/")
subprocess.call(["unzip", "-q", DATA_URL.split("/")[-1], "-d", "data/"])
subprocess.call(["mv", DATA_URL.split("/")[-1], "data/"])

logging.info("..done")
logging.info("Installing requirements")
subprocess.call(["pip3", "install", "-r", PATH_TO_PACKAGE+"requirements.txt"])
subprocess.call(["pip", "install", "tensorboard"])

logging.info("Upgrading keras")
subprocess.call(["pip3", "install", "git+git://github.com/fchollet/keras.git", "--upgrade"])

logging.info("Copying notebook to notebooks")
subprocess.call(["cp", PATH_TO_PACKAGE + "aircrafts_cnn.ipynb", "notebooks/"])
logging.info("Finished")
