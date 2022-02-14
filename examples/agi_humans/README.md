# AGI Humans in Fields Dataset
This is a 2D Object Detection dataset, collected by AGI using Robotti equipped with a front and back camera.
The dataset is split in train and test sets, and each of these is split in two subsets: a) images depicting humans, and b) images with no humans. The dataset is annotated using the [labelImg](https://github.com/tzutalin/labelImg) tool in VOC style .xml format.

## Dataset statistics
| set    | # humans | # no humans | total  |
|--------|----------|-------------|--------|
| train  |    81    |     325     |  406   |
|  test  |    79    |     324     |  403   |

## Download
The dataset can be downloaded in zip format using:
```
wget ftp://opendrdata.csd.auth.gr/datasets/agi_humans/agi_humans_v1.zip
```

If using `opendr` data format, the dataset can be downloaded automatically:
```python
from opendr_datasets import AGIHumans

path = 'data/agi_humans'
dataset = AGIHumans(path)
# the AGIHumans class will search the directory given by `path'
# if it doesn't exist or it's empty, the dataset will be downloaded
# and unzipped in the specified directory
```

## References
Citation TBA.

