#!/usr/bin/env python

import logging
import os
import subprocess
import sys

logging.basicConfig(level=logging.INFO, stream=sys.stdout)

os.environ["AIRCRAFT_DATA"] = 'data/fgvc-aircraft-2013b/data'

DATA_URL = "http://www.robots.ox.ac.uk/~vgg/data/fgvc-aircraft/archives/fgvc-aircraft-2013b.tar.gz"

logging.info("Running installation...")
subprocess.call(["mkdir", "data"])
subprocess.call(["mkdir", "notebooks"])

logging.info("Folders created")
logging.info("Downloading dataset...")
subprocess.call(["wget", DATA_URL])

logging.info("..done")
logging.info("Unpacking archive to data/")
subprocess.call(["tar", "-zxf", DATA_URL.split("/")[-1], "-C", "data/"])
subprocess.call(["mv", DATA_URL.split("/")[-1], "data/"])

logging.info("..done")
logging.info("Installing requirements")
subprocess.call(["pip3", "install", "-r", "ml_weekend_img/requirements.txt"])
subprocess.call(["pip", "install", "tensorboard"])

logging.info("Upgrading keras")
subprocess.call(["pip3", "install", "git+git://github.com/fchollet/keras.git", "--upgrade"])

logging.info("Copying notebook to notebooks")
subprocess.call(["cp", "ml_weekend_img/aircrafts_cnn.ipynb", "notebooks/"])
logging.info("Finished")
