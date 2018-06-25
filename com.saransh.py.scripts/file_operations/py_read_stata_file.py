import matplotlib.pyplot as plt
import pandas as pd

# Import sas7bdat package

from def_path import path

df = pd.read_stata(path + 'disarea.dta', 'rb')

# Print head of DataFrame
print(df.head())


# Plot histogram of DataFrame features (pandas and pyplot already imported)
def plot(key):
    if key not in ['wbcode', 'country']:
        pd.DataFrame.hist(df[[key]])
        plt.ylabel('count')
        plt.show()

for key in df.keys():
    plot(key)


