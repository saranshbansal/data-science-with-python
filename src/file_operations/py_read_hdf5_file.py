import h5py

from env import path

# Assign filename: file
file = 'NEONDS.hdf5'

# Load file: data
data = h5py.File(path + file, 'r')

# Print the datatype of the loaded file
print(type(data))

# Print the keys of the file
for key in data.keys():
    print(data[key])
