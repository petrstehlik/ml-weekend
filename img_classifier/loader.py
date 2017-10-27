from PIL import Image, ImageOps
import numpy as np
from tqdm import tqdm
import multiprocessing
import os


def load_image(infilename):
    img = Image.open(infilename).convert('L')
    img.load()
    width, height = img.size
    img.crop((0, 0, width, height - 20))
    img = ImageOps.fit(img, [150, 100], Image.ANTIALIAS)
    data = np.asarray(img, dtype="uint8")
    return data


def load_dataset(designation, classes, n_jobs=1, n_samples=None):
    if not (n_jobs == 0 or n_jobs == 1):
        return load_dataset_multiproc(designation, classes, n_jobs=n_jobs, n_samples=n_samples)

    class_numbers = []
    print("Loading {}...".format(designation))
    result = []
    file_name = '{}/{}.txt'.format(os.environ.get("AIRCRAFT_DATA"), designation)
    with open(file_name) as f:
        for i, line in tqdm(enumerate(f)):
            if n_samples and n_samples < i:
                break

            file_desig = line.split()[0]
            file_class = line.split(None, maxsplit=1)[1].strip()
            class_numbers.append(classes[file_class])
            img = load_image("{}/images/{}.jpg".format(os.environ.get("AIRCRAFT_DATA"), file_desig))
            result.append(img)
    result = np.array(result)
    class_numbers = np.array(class_numbers)
    print('first result: ', repr(result[0]))
    print('Giving back array of {} images and {} classes'.format(len(result), len(class_numbers)))
    return result, class_numbers


def load_dataset_multiproc(designation, classes, n_jobs=-1, n_samples=None):
    print("Loading {}...".format(designation))
    file_name = '{}/{}.txt'.format(os.environ.get("AIRCRAFT_DATA"), designation)

    tasks = []
    with open(file_name) as f:
        for i, line in enumerate(tqdm(f)):
            if n_samples and n_samples < i:
                break
            tasks.append(line)

    pool = multiprocessing.Pool(n_jobs)

    result, class_numbers = [], []
    for r, c in pool.map_async(_load_dataset, tasks).get(

    ):
        result.append(r)
        class_numbers.append(c)

    result = np.array(result)
    class_numbers = np.array(class_numbers)
    print('first result: ', repr(result[0]))
    print('Giving back array of {} images and {} classes'.format(len(result), len(class_numbers)))
    return result, class_numbers


def _load_dataset(line):
    file_desig = line.split()[0]
    file_class = line.split(None, maxsplit=1)[1].strip()
    img = load_image("{}/images/{}.jpg".format(os.environ.get("AIRCRAFT_DATA"), file_desig))
    return img, file_class


def load_classes(designation):
    classes = {}
    with open('{}/{}.txt'.format(os.environ.get("AIRCRAFT_DATA"), designation)) as f:
        for i, line in enumerate(f):
            classes[line.strip()] = i
    return classes


def load_data(n_jobs=1, n_train=None, n_test=None):
    classes = load_classes('manufacturers')
    (x_train, y_train) = load_dataset('images_manufacturer_train', classes, n_jobs, n_samples=n_train)
    (x_test, y_test) = load_dataset('images_manufacturer_test', classes, n_jobs, n_samples=n_test)

    return (x_train, y_train), (x_test, y_test)
