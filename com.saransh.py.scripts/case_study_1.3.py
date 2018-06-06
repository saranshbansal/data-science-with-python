import pandas as pd
import matplotlib.pyplot as plt

# Writing an iterator to load data in chunks (1)
#
# Another way to read data too large to store in memory in chunks is to read the file in as DataFrames of a certain
# length, say, 100. For example, with the pandas package (imported as pd), you can do
# pd.read_csv(filename, chunksize=100). This creates an iterable reader object, which means that you can use next()
# on it.
#
# In this exercise, you will read a file in small DataFrame chunks with read_csv(). You're going to use the World
# Bank Indicators data 'ind_pop_data.csv', available in your current directory, to look at the urban population indicator
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
urb_pop_reader = pd.read_csv('../resources/ind_pop_data.csv', chunksize=1000)

# Get the first DataFrame chunk: df_urb_pop
df_urb_pop = next(urb_pop_reader)

# Check out the head of the DataFrame
print(df_urb_pop.head())

# Check out specific country: df_pop_ceb
df_pop_ceb = df_urb_pop[df_urb_pop['CountryCode'] == 'CEB']

# Zip DataFrame columns of interest: pops
pops = zip(df_pop_ceb['Total Population'], df_pop_ceb['Urban population (% of total)'])

# Turn zip object into list: pops_list
pops_list = list(pops)

# Print pops_list
print(pops_list)

# Writing an iterator to load data in chunks (3)
# You're getting used to reading and processing data in chunks by now.
# Let's push your skills a little further by adding a column to a DataFrame.
#
# In this exercise, you will be using a list comprehension to create the values for a new column 'Total Urban
# Population' from the list of tuples that you generated earlier. Recall from the previous exercise that the first
# and second elements of each tuple consist of, respectively, values from the columns 'Total Population' and 'Urban
# population (% of total)'. The values in this new column 'Total Urban Population', therefore, are the product of the
#  first and second element in each tuple. Furthermore, because the 2nd element is a percentage, you need to divide
# the entire result by 100, or alternatively, multiply it by 0.01.
#
# You will also plot the data from this new column to create a visualization of the urban population data.
#
# You're going to use the data from 'ind_pop_data.csv', available in your current directory. The packages pandas and
# matplotlib.pyplot have been imported as pd and plt respectively for your use.

# Initialize reader object: urb_pop_reader(see above)

# Get the first DataFrame chunk: df_urb_pop(see above)

# Check out specific country: df_pop_ceb(see above)

# Zip DataFrame columns of interest: pops(see above)

# Turn zip object into list: pops_list(see above)

# Use list comprehension to create new DataFrame column 'Total Urban Population'
df_pop_ceb['Total Urban Population'] = [int(tup[0] * tup[1] * 0.01) for tup in pops_list]
print(df_pop_ceb['Total Urban Population'])

# Plot urban population data
df_pop_ceb.plot(kind="scatter", x='Year', y='Total Urban Population')
plt.show()

# Writing an iterator to load data in chunks (4)
#
# In the previous exercises, you've only processed the data from the
# first DataFrame chunk. This time, you will aggregate the results over all the DataFrame chunks in the dataset. This
#  basically means you will be processing the entire dataset now. This is neat because you're going to be able to
# process the entire large dataset by just working on smaller pieces of it!
#
# You're going to use the data from 'ind_pop_data.csv', available in your current directory. The packages pandas and
# matplotlib.pyplot have been imported as pd and plt respectively for your use.

# Initialize reader object: urb_pop_reader(see above)

# Initialize empty DataFrame: data
data = pd.DataFrame()

# Iterate over each DataFrame chunk
for df_urb_pop in urb_pop_reader:
    # Check out specific country: df_pop_ceb(see above)

    # Zip DataFrame columns of interest: pops(see above)

    # Turn zip object into list: pops_list(see above)

    # Use list comprehension to create new DataFrame column 'Total Urban Population1'(similar to above)
    df_pop_ceb['Total Urban Population1'] = [int(tup[0] * tup[1]) for tup in pops_list]

    # Append DataFrame chunk to data: data
    data = data.append(df_pop_ceb)

# Plot urban population data
data.plot(kind='scatter', x='Year', y='Total Urban Population1')
plt.show()