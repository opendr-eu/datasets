from setuptools import setup

setup(
    name='opendr_datasets',
    version='0.1.0',
    description='OpenDR format datasets',
    url='https://github.com/opendr-eu/datasets',
    packages=['opendr_datasets',
              'opendr_datasets.object_detection_2d'],
    package_dir={"": "src"}
)
