# ActiveFace dataset

## Dataset Description

The synthetic face image dataset was generated using Unity’s Perception package.
It consists of 175428 face images taken at different environments, lighting conditions, camera distances and angles. 
In total, the dataset contains images for 8 environments, 33 humans, 4 lighting conditions, 7 camera distances (1m-4m) and 36 camera angles (0-360 at 10-degree intervals). 
The dataset does not include images at every single combination of available camera distances and angles, since for some values the camera would collide with another object or go outside the confines of an environment. 
As a result, some combinations of camera distances and angles do not exist in the dataset.

## How to download

Not yet available. Links will be provided soon.

## Folder Configuration

The dataset consists of 33 main folders each one containing all the face images for one human. 
Each main folder consists of 32 subfolders, each one containing that person’s face images for one combination of environment and lighting condition. 
Each subfolder is named "x_y", where "x" denotes the id of the environment and "y" denotes the id of the lighting condition.

## Naming Conventions

Each image is named “e_h_l_d_r.jpg”, where:
- **e** denotes the id of the environment. 
- **h** denotes the id of the person.
- **l** denotes the id of the lighting condition.
- **d** denotes the camera distance at which the image was captured.
- **r** denotes the camera angle at which the image was captured.



