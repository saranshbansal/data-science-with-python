import pandas as pd

# Writing an iterator to load data in chunks (1)
#
# Another way to read data too large to store in memory in chunks is to read the file in as DataFrames of a certain
# length, say, 100. For example, with the pandas package (imported as pd), you can do
# pd.read_csv(filename, chunksize=100). This creates an iterable reader object, which means that you can use next()
# on it.
#
# In this exercise, you will read a file in small DataFrame chunks with read_csv(). You're going to use the World
# Bank Indicators data 'ind_pop.csv', available in your current directory, to look at the urban population indicator
# for numerous countries and years.
# Import the pandas package

# Initialize reader object: df_reader
df_reader = pd.read_csv('../resources/WDIData_min.csv', chunksize=10)

# Print two chunks
print(next(df_reader))
print(next(df_reader))

# Writing an iterator to load data in chunks (2)
#
# In the previous exercise, you used read_csv() to read in DataFrame chunks from a large dataset. In this exercise,
# you will read in a file using a bigger DataFrame chunk size and then process the data from the first chunk.
#
# To process the data, you will create another DataFrame composed of only the rows from a specific country. You will
# then zip together two of the columns from the new DataFrame, 'Total Population' and 'Urban population (% of
# total)'. Finally, you will create a list of tuples from the zip object, where each tuple is composed of a value
# from each of the two columns mentioned.
#
# You're going to use the data from 'ind_pop_data.csv', available in your current directory. Pandas has been imported
#  as pd.

# Initialize reader object: urb_pop_reader
urb_pop_reader = pd.read_csv('../resources/WDIData_min.csv', chunksize=1000)

# Get the first DataFrame chunk: df_urb_pop
df_urb_pop = next(urb_pop_reader)

# Check out the head of the DataFrame
print(df_urb_pop.head())

# Check out specific country: df_pop_ceb
df_pop_ceb = df_urb_pop[lambda cc: cc['Country Code'] == 'CEB']

# Zip DataFrame columns of interest: pops
pops = zip(df_pop_ceb['Indicator Name'], df_pop_ceb['2017'])

# Turn zip object into list: pops_list
pops_list = list(pops)

# Print pops_list
print(pops_list)
