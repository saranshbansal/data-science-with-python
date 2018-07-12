# Metrics for classification
#
# In Chapter 1, you evaluated the performance of your k-NN classifier based on its
# accuracy. However, as Andy discussed, accuracy is not always an informative metric. In this exercise, you will dive
#  more deeply into evaluating the performance of binary classifiers by computing a confusion matrix and generating a
#  classification report.
#
# You may have noticed in the video that the classification report consisted of three rows, and an additional support
#  column. The support gives the number of samples of the true response that lie in that class - so in the video
# example, the support was the number of Republicans or Democrats in the test set on which the classification report
# was computed. The precision, recall, and f1-score columns, then, gave the respective metrics for that particular
# class.
#
# Here, you'll work with the PIMA Indians dataset obtained from the UCI Machine Learning Repository. The goal is to
# predict whether or not a given female patient will contract diabetes based on features such as BMI, age,
# and number of pregnancies. Therefore, it is a binary classification problem. A target value of 0 indicates that the
#  patient does not have diabetes, while a value of 1 indicates that the patient does have diabetes. As in Chapters 1
#  and 2, the dataset has been preprocessed to deal with missing values.
#
# The dataset has been loaded into a DataFrame df and the feature and target variable arrays X and y have been
# created for you. In addition, sklearn.model_selection.train_test_split and sklearn.neighbors.KNeighborsClassifier
# have already been imported.
#
# Your job is to train a k-NN classifier to the data and evaluate its performance by generating a confusion matrix
# and classification report.


# Import numpy and pandas
import pandas as pd
from sklearn.model_selection import train_test_split
# Import necessary modules
from sklearn.neighbors import KNeighborsClassifier

from def_path import path

# Read the CSV file into a DataFrame: df
df = pd.read_csv(path + 'diabetes.csv')

# Create arrays for features and target variable
X = df['age'].values
y = df['diabetes'].values

# Reshape X and y
X = X.reshape(-1, 1)
y = y.reshape(-1, 1)

# Import necessary modules
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

# Create training and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42)

# Instantiate a k-NN classifier: knn
knn = KNeighborsClassifier(n_neighbors=6)

# Fit the classifier to the training data
knn.fit(X_train, y_train)

# Predict the labels of the test data: y_pred
y_pred = knn.predict(X_test)

# Generate the confusion matrix and classification report
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
