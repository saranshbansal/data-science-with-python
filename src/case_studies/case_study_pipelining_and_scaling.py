# Bringing it all together II:
#
# Pipeline for regression For this final exercise, you will return to the Gapminder
# dataset. Guess what? Even this dataset has missing values that we dealt with for you in earlier chapters! Now,
# you have all the tools to take care of them yourself!
#
# Your job is to build a pipeline that imputes the missing data, scales the features, and fits an ElasticNet to the
# Gapminder data. You will then tune the l1_ratio of your ElasticNet using GridSearchCV.
#
# All the necessary modules have been imported, and the feature and target variable arrays have been pre-loaded as X
# and y.

import numpy as np
import pandas as pd
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import Imputer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import ElasticNet

from env import path

# Read 'gm_2008_region.csv' into a DataFrame: df
df = pd.read_csv(path + 'gm_2008_region.csv')

X = df.drop('life', axis=1)
y = df['life']

# Setup the pipeline steps: steps
steps = [('imputation', Imputer(missing_values='NaN', strategy='mean', axis=0)),
         ('scaler', StandardScaler()),
         ('elasticnet', ElasticNet())]

# Create the pipeline: pipeline
pipeline = Pipeline(steps)

# Specify the hyperparameter space
parameters = {'elasticnet__l1_ratio': np.linspace(0, 1, 30)}

# Create train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42)

# Create the GridSearchCV object: gm_cv
gm_cv = GridSearchCV(pipeline, param_grid=parameters)

# Fit to the training set
gm_cv.fit(X_train, y_train)

# Compute and print the metrics
r2 = gm_cv.score(X_test, y_test)
print("Tuned ElasticNet Alpha: {}".format(gm_cv.best_params_))
print("Tuned ElasticNet R squared: {}".format(r2))
