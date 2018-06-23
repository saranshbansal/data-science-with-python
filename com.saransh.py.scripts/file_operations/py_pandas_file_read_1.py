# Import pandas as pd
import pandas as pd
path = '../resources/'
# Assign the filename: file
file = 'digits.csv'

# Read the file into a DataFrame: df
df = pd.read_csv(file)

# View the head of the DataFrame
print(df.head())
