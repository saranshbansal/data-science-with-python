# Import package
import scipy.io
import matplotlib.pyplot as plt
import numpy as np

from env import path

# Load MATLAB file: mat
mat = scipy.io.loadmat(path + 'albeck_gene_expression.mat')

# Print the datatype type of mat
print(type(mat))

# Print the keys of the MATLAB dictionary
print(mat.keys())

# Print the type of the value corresponding to the key 'CYratioCyt'
print(type(mat['fret']))

# Print the shape of the value corresponding to the key 'CYratioCyt'
print(np.shape(mat['fret']))

# Subset the array and plot it
data = mat['fret'][25, 5:]
fig = plt.figure()
plt.plot(data)
plt.xlabel('time (min.)')
plt.ylabel('normalized fluorescence (measure of expression)')
plt.show()

