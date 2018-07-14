# Regression with categorical features
#
# Having created the dummy variables from the 'Region' feature, you can build
# regression models as you did before. Here, you'll use ridge regression to perform 5-fold cross-validation.
# The feature array X and target variable array y have been pre-loaded.
#
# Dropping missing data
#
# The voting dataset from Chapter 1 contained a bunch of missing values that we dealt with for
# you behind the scenes. Now, it's time for you to take care of these yourself!
#
# The unprocessed dataset has been loaded into a DataFrame df. Explore it in the IPython Shell with the .head()
# method. You will see that there are certain data points labeled with a '?'. These denote missing values. As you saw
#  in the video, different datasets encode missing values in different ways. Sometimes it may be a '9999',
# other times a 0 - real-world data can be very messy! If you're lucky, the missing values will already be encoded as
#  NaN. We use NaN because it is an efficient and simplified way of internally representing missing data, and it lets
#  us take advantage of pandas methods such as .dropna() and .fillna(), as well as scikit-learn's Imputation
# transformer Imputer().
# In this exercise, your job is to convert the '?'s to NaNs, and then drop the rows that contain them from the
# DataFrame.

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from def_path import path

# Read 'gapminder.csv' into a DataFrame: df
df = pd.read_csv(path + 'gm_2008_region.csv')

# Create a boxplot of life expectancy per region
df.boxplot('life', 'Region', rot=60)

# Show the plot
plt.show()

# ----------------------

# Create arrays for features and target variable
X = df['population'].values
y = df['life'].values

# Reshape X and y
X = X.reshape(-1, 1)
y = y.reshape(-1, 1)

# Import necessary modules
from sklearn.linear_model import Ridge
from sklearn.model_selection import cross_val_score

# Instantiate a ridge regressor: ridge
ridge = Ridge(alpha=0.5, normalize=True)

# Perform 5-fold cross-validation: ridge_cv
ridge_cv = cross_val_score(ridge, X, y, cv=5)

# Print the cross-validated scores
print(ridge_cv)

# -------------------------

# Convert '?' to NaN
df[df == '?'] = np.nan

# Print the number of NaNs
print(df.isnull().sum())

# Print shape of original DataFrame
print("Shape of Original DataFrame: {}".format(df.shape))

# Drop missing values and print shape of new DataFrame
df = df.dropna()

# Print shape of new DataFrame
print("Shape of DataFrame After Dropping All Rows with Missing Values: {}".format(df.shape))
