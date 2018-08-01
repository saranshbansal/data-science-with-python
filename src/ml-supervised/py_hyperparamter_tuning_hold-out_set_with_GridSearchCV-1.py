# Hold-out set in practice I: Classification
#
# You will now practice evaluating a model with tuned hyperparameters on a
#  hold-out set. The feature array and target variable array from the diabetes dataset have been pre-loaded as X and y.
#
# In addition to C, logistic regression has a 'penalty' hyperparameter which specifies whether to use 'l1' or 'l2'
# regularization. Your job in this exercise is to create a hold-out set, tune the 'C' and 'penalty' hyperparameters
# of a logistic regression classifier using GridSearchCV on the training set, and then evaluate its performance
# against the hold-out set.

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split

from helper import path

# Read the CSV file into a DataFrame: df
df = pd.read_csv(path + 'diabetes.csv')

# Create arrays for features and target variable
X = df.drop('diabetes', axis=1)
y = df['diabetes']

# Create the hyperparameter grid
c_space = np.logspace(-5, 8, 15)
param_grid = {'C': c_space, 'penalty': ['l1', 'l2']}

# Instantiate the logistic regression classifier: logreg
logreg = LogisticRegression()

# Create train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42)

# Instantiate the GridSearchCV object: logreg_cv
logreg_cv = GridSearchCV(logreg, param_grid, cv=5)

# Fit it to the training data
logreg_cv.fit(X_train, y_train)

# Print the optimal parameters and best score
print("Tuned Logistic Regression Parameter: {}".format(logreg_cv.best_params_))
print("Tuned Logistic Regression Accuracy: {}".format(logreg_cv.best_score_))
