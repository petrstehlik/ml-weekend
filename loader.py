import os
from collections import namedtuple

BoundingBox = namedtuple('BoundingBox', ('xmin', 'ymin', 'xmax', 'ymax'))


class Dataset:
    """
    Dataset wrapper for FGVC-Aircraft available at:
    http://www.robots.ox.ac.uk/~vgg/data/fgvc-aircraft/

    The usage of this data has been granted *exclusively for non-commercial research purposes* only.
    More information abou tthe dataset can be found at:
    https://arxiv.org/abs/1306.5151
    """

    PATH = './data/fgvc-aircraft-2013b/data'

    def _load_one_split(self, anot_name):
        file_path = os.path.join(self.PATH, f'{anot_name}.txt')
        return dict(row.rstrip('\n').split(' ', 1) for row in open(file_path).readlines())

    def _load_set(self, set_name):
        file_path = os.path.join(self.PATH, f'{set_name}.txt')
        return [row.rstrip('\n') for row in open(file_path).readlines()]

    def families(self):
        return self._load_set('families')

    def manufacturers(self):
        return self._load_set('manufacturers')

    def variants(self):
        return self._load_set('variants')

    def images_test(self):
        return self._load_set('images_test')

    def images_train(self):
        return self._load_set('images_train')

    def images_val(self):
        return self._load_set('images_val')

    def images_box(self):
        file_path = os.path.join(self.PATH, 'images_box.txt')
        image_boxes = {}
        for row in open(file_path).readlines():
            serial, *coors = row.rstrip('\n').split(' ')
            image_boxes[serial] = BoundingBox(*(int(coor) for coor in coors))
        return image_boxes

    # family
    def images_family_test(self):
        return self._load_one_split('images_family_test')

    def images_family_train(self):
        return self._load_one_split('images_family_train')

    def images_family_trainval(self):
        return self._load_one_split('images_family_trainval')

    def images_family_val(self):
        return self._load_one_split('images_family_val')

    # manufacturer
    def images_manufacturer_test(self):
        return self._load_one_split('images_manufacturer_test')

    def images_manufacturer_train(self):
        return self._load_one_split('images_manufacturer_train')

    def images_manufacturer_trainval(self):
        return self._load_one_split('images_manufacturer_trainval')

    def images_manufacturer_val(self):
        return self._load_one_split('images_manufacturer_val')

    # variant
    def images_variant_test(self):
        return self._load_one_split('images_variant_test')

    def images_variant_train(self):
        return self._load_one_split('images_variant_train')

    def images_variant_trainval(self):
        return self._load_one_split('images_variant_trainval')

    def images_variant_val(self):
        return self._load_one_split('images_variant_val')


if __name__ == '__main__':
    d = Dataset()
