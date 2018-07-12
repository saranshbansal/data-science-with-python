# What is Lasso Regression?
#
# http://www.statisticshowto.com/lasso-regression/
#
# Lasso regression is a type of linear
# regression that uses shrinkage. Shrinkage is where data values are shrunk towards a central point, like the mean.
# The lasso procedure encourages simple, sparse models (i.e. models with fewer parameters). This particular type of
# regression is well-suited for models showing high levels of muticollinearity or when you want to automate certain
# parts of model selection, like variable selection/parameter elimination.
#
# The acronym “LASSO” stands for Least Absolute Shrinkage and Selection Operator. Lasso regression is what is called
# the Penalized regression method, often used in machine learning to select the subset of variables. It is a
# supervised machine learning method. Specifically, LASSO is a Shrinkage and Variable Selection method for linear
# regression models. LASSO, is actually an acronym for Least Absolute Selection and Shrinkage Operator.
#
# 0:34
#
# The LASSO imposes a constraint on the sum of the absolute values of the model parameters, where the sum has a
# specified constant as an upper bound. This constraint causes regression coefficients for some variables to shrink
# towards zero. This is the shrinkage process. The shrinkage process allows for better interpretation of the model
# and identifies the variables most strongly associated with the target corresponds variable. That is the variable
# selection process. It goes to obtain the subset of predictors that minimizes prediction error.
#
# So why use Lasso instead of just using ordinary least squares multiple regression?
#
# Well, first, it can provide greater prediction accuracy. If the true relationship between the response variable and
#  the predictors is approximately linear and you have a large number of observations, then OLS regression parameter
# estimates will have low bias and low variance. However, if you have a relatively small number of observations and a
#  large number of predictors, then the variance of the OLS perimeter estimates will be higher. In this case,
# Lasso Regression is useful because shrinking the regression coefficient can reduce variance without a substantial
# increase in bias. 1:43 Second, Lasso Regression can increase model interpretability. Often times, at least some of
# the explanatory variables in an OLS multiple regression analysis are not really associated with the response
# variable. As a result, we often end up with a model that's over fitted and more difficult to interpret. With Lasso
# Regression, the regression coefficients for unimportant variables are reduced to zero which effectively removes
# them from the model and produces a simpler model that selects only the most important predictors. In Lasso
# Regression, a tuning parameter called lambda is applied to the regression model to control the strength of the
# penalty. As lambda increases, more coefficients are reduced to zero that is fewer predictors are selected and there
#  is more shrinkage of the non-zero coefficient. With Lasso Regression where lambda is equal to zero then we have an
#  OLS regression analysis. Bias increases and variance decreases as lambda increases. To demonstrate how lasso
# regression works, let's use and example from the ad help data set in which our goal is to identify a set of
# variables that best predicts the extent to which students feel connected to their school. We will use the same
# ad-health data set that we used for the decision tree in random forced machine learning applications. The response
# or target variable is a quantitative variable that measures school connectedness. The response values range from 6
# to 38, where higher values indicate a greater connection with the school. There are a total of 23 Categorical and
# Quantitative predictor variables. This is a pretty large number of predictor variables, so using OLS multiple
# regression analysis would not be ideal, particularly if the goal is to identify a smaller subset of these
# predictors that most accurately predicts school connectedness. Categorical predictors include gender and race and
# ethnicity. Although Lasso Regression models can handle categorical variables with more than two levels In
# conducting my data management, I created a series of five binary categorical variables for race and ethnicity,
# Hispanic, White, Black, Native American, and Asian. I did this to improve interpratability of the selected model.
# Binary substitutes variables for measure with individual questions of about whether the adolescent had ever used
# alcohol, marijuana, cocaine, or inhalants. Additional categorical variables include the availability of cigarettes
# in the home, whether or not either parent was on public assistance, and any experience with being expelled from
# school. Finally, quantitative predictive variables include age, alcohol problems, and a measure of deviance. That
# includes such behaviors as vandalism, other property damage, lying, stealing, running away,

import matplotlib.pyplot as plt
# Import the necessary modules
import pandas as pd
# Import Lasso
from sklearn.linear_model import Lasso

from def_path import path

# Read the CSV file into a DataFrame: df
df = pd.read_csv(path + 'gm_2008_region.csv')
print(df.info())
print(df.describe())
print(df.head())

# Create arrays for features and target variable
X = df['population'].values
y = df['life'].values

# Reshape X and y
X = X.reshape(-1, 1)
# y = y.reshape(-1, 1)

# Instantiate a lasso regressor: lasso
lasso = Lasso(alpha=0.4, normalize=True)

# Fit the regressor to the data
lasso.fit(X, y)

# Compute and print the coefficients
lasso_coef = lasso.coef_
print(lasso_coef)

df_columns = df.keys()
print(df_columns)

# Plot the coefficients
plt.plot(range(len(df_columns)), lasso_coef)
plt.xticks(range(len(df_columns)), df_columns.values, rotation=60)
plt.margins(0.02)
plt.show()
