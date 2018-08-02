'''
PCA doesn't learn parts

Unlike NMF, PCA doesn't learn the parts of things. Its components do not correspond to topics (in the case of documents) or to parts of images, when trained on images. Verify this for yourself by inspecting the components of a PCA model fit to the dataset of LED digit images from the previous exercise. The images are available as a 2D array samples. Also available is a modified version of the show_as_image() function which colors a pixel red if the value is negative.

After submitting the answer, notice that the components of PCA do not represent meaningful parts of images of LED digits!

INSTRUCTIONS
100XP
Import PCA from sklearn.decomposition.
Create a PCA instance called model with 7 components.
Apply the .fit_transform() method of model to samples. Assign the result to features.
To each component of the model (accessed via model.components_), apply the show_as_image() function to that component inside the loop.
'''
import csv

import numpy as np
# Import pyplot
from matplotlib import pyplot as plt
# Import PCA
from sklearn.decomposition import PCA

from helper import path

with open('../' + path + 'lcd-digits.csv', 'r') as f:
    samples = list(csv.reader(f, delimiter=','))
    samples = np.array(samples).astype(np.float)


def show_as_image(sample):
    bitmap = sample.reshape((13, 8))
    bitmap[bitmap >= 0] = 1
    bitmap[bitmap < 0] = 0
    plt.figure()
    plt.imshow(bitmap, cmap='gist_yarg', interpolation='nearest', vmin=-.1, vmax=1.1)
    plt.colorbar()
    plt.show()


# Create a PCA instance: model
model = PCA(n_components=7)

# Apply fit_transform to samples: features
features = model.fit_transform(samples)

# Call show_as_image on each component
for component in model.components_:
    show_as_image(component)
