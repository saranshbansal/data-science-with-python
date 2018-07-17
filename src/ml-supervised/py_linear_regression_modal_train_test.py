# Fit & predict for regression
# Import numpy and pandas
import numpy as np
import pandas as pd
# Import necessary modules
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

from env import path

# Read the CSV file into a DataFrame: df
df = pd.read_csv(path + 'gm_2008_region.csv')

# Create arrays for features and target variable
X_fertility = df['fertility'].values
y = df['life'].values

# Reshape X and y
X_fertility = X_fertility.reshape(-1, 1)
y = y.reshape(-1, 1)

# Create training and test sets
X_train, X_test, y_train, y_test = train_test_split(X_fertility, y, test_size=0.3, random_state=42)

# Create the regressor: reg_all
reg_all = LinearRegression()

# Fit the regressor to the training data
reg_all.fit(X_train, y_train)

# Predict on the test data: y_pred
y_pred = reg_all.predict(X_test)

# Compute and print R^2 and RMSE
print("R^2: {}".format(reg_all.score(X_test, y_test)))
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print("Root Mean Squared Error: {}".format(rmse))
