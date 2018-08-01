# Bringing it all together I:
#
# Pipeline for classification It is time now to piece together everything you have
# learned so far into a pipeline for classification! Your job in this exercise is to build a pipeline that includes
# scaling and hyperparameter tuning to classify wine quality.
#
# You'll return to using the SVM classifier you were briefly introduced to earlier in this chapter. The
# hyperparameters you will tune are C and gamma. C controls the regularization strength. It is analogous to the C you
#  tuned for logistic regression in Chapter 3, while gamma controls the kernel coefficient: Do not worry about this
# now as it is beyond the scope of this course.
#
# The following modules have been pre-loaded: Pipeline, svm, train_test_split, GridSearchCV, classification_report,
# accuracy_score. The feature and target variable arrays X and y have also been pre-loaded.e.

import pandas as pd
from sklearn.metrics import classification_report
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

from helper import path

# Read 'white-wine.csv' into a DataFrame: df
df = pd.read_csv(path + 'white-wine.csv')

X = df.drop('quality', axis=1)
y = df['quality']

# Setup the pipeline
steps = [('scaler', StandardScaler()),
         ('SVM', SVC())]

pipeline = Pipeline(steps)

# Specify the hyperparameter space
parameters = {'SVM__C': [1, 10, 100],
              'SVM__gamma': [0.1, 0.01]}

# Create train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=21)

# Instantiate the GridSearchCV object: cv
cv = GridSearchCV(pipeline, param_grid=parameters)

# Fit to the training set
cv.fit(X_train, y_train)

# Predict the labels of the test set: y_pred
y_pred = cv.predict(X_test)

# Compute and print metrics
print("Accuracy: {}".format(cv.score(X_test, y_test)))
print(classification_report(y_test, y_pred))
print("Tuned Model Parameters: {}".format(cv.best_params_))
