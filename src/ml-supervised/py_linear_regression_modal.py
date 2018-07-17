# Fit & predict for regression
#
# Now, you will fit a linear regression and predict life expectancy using just one
# feature. You saw Andy do this earlier using the 'RM' feature of the Boston housing dataset. In this exercise,
# you will use the 'fertility' feature of the Gapminder dataset. Since the goal is to predict life expectancy,
# the target variable here is 'life'. The array for the target variable has been pre-loaded as y and the array for
# 'fertility' has been pre-loaded as X_fertility.
#
# A scatter plot with 'fertility' on the x-axis and 'life' on the y-axis has been generated. As you can see,
# there is a strongly negative correlation, so a linear regression should be able to capture this trend. Your job is
# to fit a linear regression and then predict the life expectancy, overlaying these predicted values on the plot to
# generate a regression line. You will also compute and print the R2 score using sckit-learn's .score() method.

# Import numpy and pandas
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# Import LinearRegression
from sklearn.linear_model import LinearRegression

from env import path

# Read the CSV file into a DataFrame: df
df = pd.read_csv(path + 'gm_2008_region.csv')

# Create arrays for features and target variable
X_fertility = df['fertility'].values
y = df['life'].values

# Print the dimensions of X and y before reshaping
print("Dimensions of y before reshaping: {}".format(y.shape))
print("Dimensions of X before reshaping: {}".format(X_fertility.shape))

# Reshape X and y
y = y.reshape(-1, 1)
X_fertility = X_fertility.reshape(-1, 1)

# Print the dimensions of X and y after reshaping
print("Dimensions of y after reshaping: {}".format(y.shape))
print("Dimensions of X after reshaping: {}".format(X_fertility.shape))

# Create the regressor: reg
reg = LinearRegression()

# Create the prediction space
prediction_space = np.linspace(min(X_fertility), max(X_fertility)).reshape(-1, 1)

# Fit the model to the data
reg.fit(X_fertility, y)

# Compute predictions over the prediction space: y_pred
y_pred = reg.predict(prediction_space)

# Print R^2
print(reg.score(X_fertility, y))

# Plot regression line over original scatter plot
plt.scatter(X_fertility, y, color='blue')
plt.plot(prediction_space, y_pred, color='black', linewidth=3)
plt.show()
