'''
Clustering stocks using KMeans

In this exercise, you'll cluster companies using their daily stock price movements (i.e. the dollar difference between the closing and opening prices for each trading day). You are given a NumPy array movements of daily price movements from 2010 to 2015 (obtained from Yahoo! Finance), where each row corresponds to a company, and each column corresponds to a trading day.

Some stocks are more expensive than others. To account for this, include a Normalizer at the beginning of your pipeline. The Normalizer will separately transform each company's stock price to a relative scale before the clustering begins.

Note that Normalizer() is different to StandardScaler(), which you used in the previous exercise. While StandardScaler() standardizes features (such as the features of the fish data from the previous exercise) by removing the mean and scaling to unit variance, Normalizer() rescales each sample - here, each company's stock price - independently of the other.

KMeans and make_pipeline have already been imported for you.

INSTRUCTIONS
100XP
INSTRUCTIONS
100XP
Import Normalizer from sklearn.preprocessing.
Create an instance of Normalizer called normalizer.
Create an instance of KMeans called kmeans with 10 clusters.
Using make_pipeline(), create a pipeline called pipeline that chains normalizer and kmeans.
Fit the pipeline to the movements array.
'''
from sklearn.cluster import KMeans
# Import Normalizer
from sklearn.preprocessing import Normalizer

# Create a normalizer: normalizer
normalizer = Normalizer()

# Create a KMeans model with 10 clusters: kmeans
kmeans = KMeans(n_clusters=10)

# Make a pipeline chaining normalizer and kmeans: pipeline
pipeline = make_pipeline(normalizer, kmeans)

# Fit pipeline to the daily price movements
pipeline.fit(movements)

'''
Which stocks move together?

In the previous exercise, you clustered companies by their daily stock price movements. So which company have stock 
prices that tend to change in the same way? You'll now inspect the cluster labels from your clustering to find out. 

Your solution to the previous exercise has already been run. Recall that you constructed a Pipeline pipeline
containing a KMeans model and fit it to the NumPy array movements of daily stock movements. In addition,
a list companies of the company names is available.

INSTRUCTIONS 100XP INSTRUCTIONS 100XP Import pandas as pd. Use the .predict() method of the pipeline to predict the
labels for movements. Align the cluster labels with the list of company names companies by creating a DataFrame df
with labels and companies as columns. This has been done for you. Use the .sort_values() method of df to sort the
DataFrame by the 'labels' column, and print the result. Hit 'Submit Answer' and take a moment to see which companies
are together in each cluster! '''
# Import pandas
import pandas as pd

# Predict the cluster labels: labels
labels = pipeline.predict(movements)

# Create a DataFrame aligning labels and companies: df
df = pd.DataFrame({'labels': labels, 'companies': companies})

# Display df sorted by cluster label
print(df.sort_values('labels'))
