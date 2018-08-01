# Imputing missing data in a ML Pipeline I
#
# As you've come to appreciate, there are many steps to building a model,
# from creating training and test sets, to fitting a classifier or regressor, to tuning its parameters, to evaluating
#  its performance on new data. Imputation can be seen as the first step of this machine learning process,
# the entirety of which can be viewed within the context of a pipeline. Scikit-learn provides a pipeline constructor
# that allows you to piece together these steps into one process and thereby simplify your workflow.
#
# You'll now practice setting up a pipeline with two steps: the imputation step, followed by the instantiation of a
# classifier. You've seen three classifiers in this course so far: k-NN, logistic regression, and the decision tree.
# You will now be introduced to a fourth one - the Support Vector Machine, or SVM. For now, do not worry about how it
#  works under the hood. It works exactly as you would expect of the scikit-learn estimators that you have worked
# with previously, in that it has the same .fit() and .predict() methods as before.


# Import the Imputer module
from sklearn.preprocessing import Imputer
from sklearn.svm import SVC

# Setup the Imputation transformer: imp
imp = Imputer(missing_values='NaN', strategy='most_frequent', axis=0)

# Instantiate the SVC classifier: clf
clf = SVC()

# Setup the pipeline with the required steps: steps
steps = [('imputation', imp),
         ('SVM', clf)]

# --------------
# Import necessary modules
import pandas as pd
from sklearn.preprocessing import Imputer
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from helper import path

# Read 'white-wine.csv' into a DataFrame: df
df = pd.read_csv(path + 'white-wine.csv')

X = df.drop('quality', axis=1)
y = df['quality']
# Setup the pipeline steps: steps
steps = [('imputation', Imputer(missing_values='NaN', strategy='most_frequent', axis=0)),
         ('SVM', SVC())]

# Create the pipeline: pipeline
pipeline = Pipeline(steps)

# Create training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Fit the pipeline to the train set
pipeline.fit(X_train, y_train)

# Predict the labels of the test set
y_pred = pipeline.predict(X_test)

# Compute metrics
print(classification_report(y_test, y_pred))
