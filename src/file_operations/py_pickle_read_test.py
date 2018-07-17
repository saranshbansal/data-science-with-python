# Save a dictionary into a pickle file.
import pickle

from env import path

d = {'Aug': '85', 'Airline': '8', 'June': '69.4', 'Mar': '84.4'}
pickle.dump(d, open(path + "data.pk1", "wb"))

# Load the dictionary back from the pickle file.
d = pickle.load(open(path + 'data.pk1', "rb"))

print(d)

print(type(d))
