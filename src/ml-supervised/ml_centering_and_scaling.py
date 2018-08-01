# Centering and scaling your data
#
# In the video, Hugo demonstrated how significantly the performance of a model can
# improve if the features are scaled. Note that this is not always the case: In the Congressional voting records
# dataset, for example, all of the features are binary. In such a situation, scaling will have minimal impact.
#
# You will now explore scaling for yourself on a new dataset - White Wine Quality! Hugo used the Red Wine Quality
# dataset in the video. We have used the 'quality' feature of the wine to create a binary target variable: If
# 'quality' is less than 5, the target variable is 1, and otherwise, it is 0.
#
# The DataFrame has been pre-loaded as df, along with the feature and target variable arrays X and y. Explore it in
# the IPython Shell. Notice how some features seem to have different units of measurement. 'density', for instance,
# only takes values between 0 and 1, while 'total sulfur dioxide' has a maximum value of 289. As a result,
# it may be worth scaling the features here. Your job in this exercise is to scale the features and compute the mean
# and standard deviation of the unscaled features compared to the scaled features.


# Import scale
import numpy as np
import pandas as pd
from sklearn.preprocessing import scale

from helper import path

# Read 'white-wine.csv' into a DataFrame: df
df = pd.read_csv(path + 'white-wine.csv')

X = df.drop('quality', axis=1)
y = df['quality']

# Scale the features: X_scaled
X_scaled = scale(X)

# Print the mean and standard deviation of the unscaled features
print("Mean of Unscaled Features: {}".format(np.mean(X)))
print("Standard Deviation of Unscaled Features: {}".format(np.std(X)))

# Print the mean and standard deviation of the scaled features
print("Mean of Scaled Features: {}".format(np.mean(X_scaled)))
print("Standard Deviation of Scaled Features: {}".format(np.std(X_scaled)))

# -----------


# Import the necessary modules
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

# Setup the pipeline steps: steps
steps = [('scaler', StandardScaler()),
         ('knn', KNeighborsClassifier())]

# Create the pipeline: pipeline
pipeline = Pipeline(steps)

# Create train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Fit the pipeline to the training set: knn_scaled
knn_scaled = pipeline.fit(X_train, y_train)

# Instantiate and fit a k-NN classifier to the unscaled data
knn_unscaled = KNeighborsClassifier().fit(X_train, y_train)

# Compute and print metrics
print('Accuracy with Scaling: {}'.format(knn_scaled.score(X_test, y_test)))
print('Accuracy without Scaling: {}'.format(knn_unscaled.score(X_test, y_test)))
