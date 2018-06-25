# Case Study: Plot Urban population trends in various countries over the years based on publically available data set.
#
# In this case study, I have to define the function plot_pop() which takes two arguments: the filename of the file to
# be processed, and the country code of the rows we want to process in the dataset.
#
# calling the function already does the following:
#
# Loading of the file chunk by chunk,
# Creating the new column of urban population values,
# and Plotting the urban population data.
#
# The function makes it convenient to repeat the same process for whatever file and country code we want to process
# and visualize!
#
# We are using the data from 'ind_pop_data.csv', available in /resources/ directory.
# The packages pandas and matplotlib.pyplot has been imported as pd and plt respectively.
#
# If you have enjoyed working with this data, you can continue exploring it using the pre-processed version available
# on Kaggle.

import pandas as pd
import matplotlib.pyplot as plt

def_file_path = '../../resources/'

# Define plot_pop()
def plot_pop(filename, country_code):
    # Initialize reader object: urb_pop_reader
    urb_pop_reader = pd.read_csv(filename, chunksize=1000)

    # Initialize empty DataFrame: data
    data = pd.DataFrame()

    # Iterate over each DataFrame chunk
    for df_urb_pop in urb_pop_reader:
        # Check out specific country: df_pop_ceb
        df_pop_ceb = df_urb_pop[df_urb_pop['CountryCode'] == country_code]

        # Zip DataFrame columns of interest: pops
        pops = zip(df_pop_ceb['Total Population'],
                   df_pop_ceb['Urban population (% of total)'])

        # Turn zip object into list: pops_list
        pops_list = list(pops)

        # Use list comprehension to create new DataFrame column 'Total Urban Population'
        df_pop_ceb['Total Urban Population'] = [int(tup[0] * tup[1]) for tup in pops_list]

        # Append DataFrame chunk to data: data
        data = data.append(df_pop_ceb)

    # Plot urban population data
    data.plot(kind='scatter', x='Year', y='Total Urban Population')
    plt.show()


# Set the filename: fn
fn = 'ind_pop_data.csv'

# Call plot_pop for country code 'CEB'
plot_pop(def_file_path + fn, 'CEB')

# Call plot_pop for country code 'ARB'
plot_pop(def_file_path + fn, 'ARB')
