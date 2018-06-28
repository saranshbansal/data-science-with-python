# Import pandas as pd
import pandas as pd
from def_path import path
# Assign the filename: file
file = 'digits.csv'

# Read the file into a DataFrame: df
df = pd.read_csv(file)

# View the head of the DataFrame
print(df.head())
