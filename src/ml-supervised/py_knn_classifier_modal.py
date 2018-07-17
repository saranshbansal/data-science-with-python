#
# k-Nearest Neighbors: Fit Having explored the Congressional voting records dataset, it is time now to build your
# first classifier. In this exercise, you will fit a k-Nearest Neighbors classifier to the voting dataset,
# which has once again been pre-loaded for you into a DataFrame df.
#
# In the video, Hugo discussed the importance of ensuring your data adheres to the format required by the
# scikit-learn API. The features need to be in an array where each column is a feature and each row a different
# observation or data point - in this case, a Congressman's voting record. The target needs to be a single column
# with the same number of observations as the feature data. We have done this for you in this exercise. Notice we
# named the feature array X and response variable y: This is in accordance with the common scikit-learn practice.
#
# Your job is to create an instance of a k-NN classifier with 6 neighbors (by specifying the n_neighbors parameter)
# and then fit it to the data. The data has been pre-loaded into a DataFrame called df. #

import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

from env import path

# this dataset won't work. Can't run this program.
file = 'house-votes-84.csv'

df = pd.read_csv(path + file)

# Explore Data
print(df.describe())

# Create arrays for the features(X) and the response variable/target(y)
X = df.drop('party', axis=1).values
y = df['party'].values

# Create a k-NN classifier with 6 neighbors
knn = KNeighborsClassifier(n_neighbors=60)

# Fit the classifier to the data
knn.fit(X, y)

# Predict the labels for the training data X
y_pred = knn.predict(X)

# This is our prediction based of knn-classifier - Prediction: ['democrat']
print(y_pred)
