import os
from urllib.request import urlretrieve
import zipfile

from opendr.perception.object_detection_2d.datasets import XMLBasedDataset, ConcatDataset
from opendr.engine.constants import OPENDR_SERVER_URL


class AGIHumans(ConcatDataset):
    def __init__(self, root, train=True):
        if not os.path.exists(root) or not os.listdir(root):
            os.mkdir(root)
            self.download(root)

        if train:
            subfolder = os.path.join(root, 'train')
        else:
            subfolder = os.path.join(root, 'test')

        human_subset = XMLBasedDataset('agi_humans', subfolder, images_dir='human', annotations_dir='human_anot')
        no_human_subset = XMLBasedDataset('agi_humans_negative', subfolder, images_dir='no_human',
                                          annotations_dir='no_human_anot')
        super().__init__([human_subset, no_human_subset])
        self.dataset_type = 'agi_humans_v1'
        self.class_names = ['person']

    @staticmethod
    def download(path, verbose=True):
        zip_file_url = OPENDR_SERVER_URL + '/datasets/agi_humans/agi_humans_v1.zip'
        if verbose:
            print("Downloading zipped data...")
        local_path = os.path.join(path, "agi_humans_v1.zip")
        urlretrieve(zip_file_url, local_path)

        if verbose:
            print("Unzipping...")
        with zipfile.ZipFile(local_path, 'r') as f:
            f.extractall(path)

    def __repr__(self):
        return f'{self.dataset_type} dataset information: \n' +\
               f'  Total images: {len(self)}'
