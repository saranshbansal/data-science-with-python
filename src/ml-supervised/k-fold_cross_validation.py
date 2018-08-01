# 5-fold cross-validation
#
# Cross-validation is a vital step in evaluating a model. It maximizes the amount of data
# that is used to train the model, as during the course of training, the model is not only trained, but also tested
# on all of the available data.
#
# In this exercise, you will practice 5-fold cross validation on the Gapminder data. By default, scikit-learn's
# cross_val_score() function uses R2 as the metric of choice for regression. Since you are performing 5-fold
# cross-validation, the function will return 5 scores. Your job is to compute these 5 scores and then take their
# average.
#
# The DataFrame has been loaded as df and split into the feature/target variable arrays X and y. The modules pandas
# and numpy have been imported as pd and np, respectively.

# Import the necessary modules
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score

from helper import path

# Read the CSV file into a DataFrame: df
df = pd.read_csv(path + 'gm_2008_region.csv')

# Create arrays for features and target variable
X = df['fertility'].values
y = df['life'].values

# Reshape X and y
X = X.reshape(-1, 1)
y = y.reshape(-1, 1)

# Create a linear regression object: reg
reg = LinearRegression()

# Compute 5-fold cross-validation scores: cv_scores
cv_scores = cross_val_score(reg, X, y, cv=5)

# Print the 5-fold cross-validation scores
print(cv_scores)

print("Average 5-Fold CV Score: {}".format(np.mean(cv_scores)))

# ---------------------------------

# Test time for 3-fold & 10 fold operations :: %timeit cross_val_score(reg, X, y, cv = ____)
# Perform 3-fold CV
cvscores_3 = cross_val_score(reg, X, y, cv=3)
print("Average 3-Fold CV Score: {}".format(np.mean(cvscores_3)))

# Perform 10-fold CV
cvscores_10 = cross_val_score(reg, X, y, cv=10)
print("Average 10-Fold CV Score: {}".format(np.mean(cvscores_10)))
