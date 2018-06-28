import pandas as pd
import matplotlib.pyplot as plt

# Import sas7bdat package
from sas7bdat import SAS7BDAT

from def_path import path

# Save file to a DataFrame: df_sas
with SAS7BDAT(path+'sales.sas7bdat') as file:
    df_sas = file.to_data_frame()

# Print head of DataFrame
print((df_sas.head()))

# Plot histogram of DataFrame features (pandas and pyplot already imported)
pd.DataFrame.hist(df_sas[['P']])
plt.ylabel('count')
plt.show()
