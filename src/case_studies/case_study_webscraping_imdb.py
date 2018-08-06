"""
Created on Mon Apr 18, 2016
@author: Honglei
Purpose: To scrapy top 250 movies in IMDB and visualize the frequency varying time
"""
import os
import re
import sys

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup

os.getcwd()  # current working directory

# get the current encoding
type = sys.getfilesystemencoding()

# request the webpage
req = requests.get("https://www.imdb.com/chart/top")
page = req.text

soup = BeautifulSoup(page, 'html.parser')
print(soup.prettify())

# get top 250 movie names and years, may take ~30 seconds
movie_names = []
movie_year = [0] * 250

j = 0
for i in range(250):
    title = str(soup.findAll('td', {'class': 'titleColumn'})[i])
    movie_names.append(re.findall('>(.*?)</a>', title)[0])

    year = str(soup.findAll('span', {'class': 'secondaryInfo'})[i])
    movie_year[i] = int(re.findall(r"\(([0-9_]+)\)", year)[0])

    # keep track of the progress
    print('Extracted movie :: ' + movie_names[i] + ' (' + str(movie_year[i]) + ') ')
    j = j + 1

print(movie_names)
print(movie_year)


def encode_title(item):
    return str(item.encode('utf-8'))


# export to the text file
open("top250names.txt", "w").write("\n".join(encode_title(item) for item in movie_names))

# compute the frequency table
y = np.bincount(movie_year)
ii = np.nonzero(y)[0]
out = list(zip(ii, y[ii]))
# create a dataframe
df = pd.DataFrame(out, columns=['Year', 'Freq'], index=ii)
# drop the first Year column since I already assign valid index
df.drop(df.columns[0], axis=1)
# plot
plt.plot(ii, df['Freq'])
plt.show()
