import csv

import numpy as np

from env import path

with open('../' + path + 'seeds-width-vs-length.csv', 'r') as f:
    grains = list(csv.reader(f, delimiter=','))
    grains = np.array(grains).astype(np.float)