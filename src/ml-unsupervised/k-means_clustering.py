import numpy as np
import pandas as pd
from sklearn.cluster import KMeans

from env import path

# Read the CSV file into a DataFrame: df
df = pd.read_csv(path + 'data_1024.csv', sep='\t')

f1 = df['Distance_Feature'].values
f2 = df['Speeding_Feature'].values

X = np.matrix(zip(f1, f2))
kmeans = KMeans(n_clusters=2).fit(X)
