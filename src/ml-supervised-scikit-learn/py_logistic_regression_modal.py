# Building a logistic regression model
#
# Time to build your first logistic regression model! As Hugo showed in the
# video, scikit-learn makes it very easy to try different models, since the Train-Test-Split/Instantiate/Fit/Predict
# paradigm applies to all classifiers and regressors - which are known in scikit-learn as 'estimators'. You'll see
# this now for yourself as you train a logistic regression model on exactly the same data as in the previous
# exercise. Will it outperform k-NN? There's only one way to find out!
#
# The feature and target variable arrays X and y have been pre-loaded, and train_test_split has been imported for you
#  from sklearn.model_selection.

# Import the necessary modules
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import train_test_split

from def_path import path

# Read the CSV file into a DataFrame: df
df = pd.read_csv(path + 'diabetes.csv')

# Create arrays for features and target variable
X = df['age'].values
y = df['diabetes'].values

# Reshape X and y
X = X.reshape(-1, 1)
y = y.reshape(-1, 1)

# Create training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42)

# Create the classifier: logreg
logreg = LogisticRegression()

# Fit the classifier to the training data
logreg.fit(X_train, y_train)

# Predict the labels of the test set: y_pred
y_pred = logreg.predict(X_test)

# Compute and print the confusion matrix and classification report
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

# -------------------------

# Plotting an ROC curve
#
# Classification reports and confusion matrices are great methods to quantitatively evaluate model performance,
# while ROC curves provide a way to visually evaluate models. As Hugo demonstrated in the video, most classifiers in
# scikit-learn have a .predict_proba() method which returns the probability of a given sample being in a particular
# class. Having built a logistic regression model, you'll now evaluate its performance by plotting an ROC curve. In
# doing so, you'll make use of the .predict_proba() method and become familiar with its functionality.
#
# Here, you'll continue working with the PIMA Indians diabetes dataset. The classifier has already been fit to the
# training data and is available as logreg

# Import necessary modules
from sklearn.metrics import roc_curve
from matplotlib import pyplot as plt

# Compute predicted probabilities: y_pred_prob
y_pred_prob = logreg.predict_proba(X_test)[:, 1]

# Generate ROC curve values: fpr, tpr, thresholds
fpr, tpr, thresholds = roc_curve(y_test, y_pred_prob)

# Plot ROC curve
plt.plot([0, 1], [0, 1], 'k--')
plt.plot(fpr, tpr)
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.show()

# -------------------------

# Calculating ROC AUC score
# Larger area under ROC curve = better model

from sklearn.metrics import roc_auc_score

print(roc_auc_score(y_test, y_pred_prob))
