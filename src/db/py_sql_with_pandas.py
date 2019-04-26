# Import necessary module
import random
from datetime import datetime

import pandas as pd
from sqlalchemy import create_engine

from helper import path

# Create engine: engine
engine = create_engine('sqlite:///' + path + 'Chinook.sqlite');

# Execute query and store records in DataFrame: df
df1 = pd.read_sql_query('select * from Album', engine)

# Execute query and store records in DataFrame: df
df2 = pd.read_sql_query('select * from Employee where EmployeeId >= 6 order by BirthDate', engine)

df3 = pd.read_sql_query('select Title, Name from Album al inner join Artist ar on al.ArtistID=ar.ArtistID', engine)

df4 = pd.read_sql_query(
    'select * from PlaylistTrack INNER JOIN Track on PlaylistTrack.TrackId = Track.TrackId where Milliseconds < 250000',
    engine)

rand_dates = [datetime(random.randrange(2000, 2001), random.randrange(1, 6), random.randrange(1, 3)) for d in
              range(0, len(df4))]
df4['dates'] = rand_dates

df4 = df4.loc[:, ~df4.columns.duplicated()]
# Print head of DataFrame
# print(df1.head())
# print(df2.head())
# print(df3.head())
# print(df4.head())
df4 = df4.groupby([df4.dates.dt.year.rename('year'), df4.dates.dt.month.rename('month')]).size()
print(df4)
# df4.groupby(df4.dates).agg({'count'})
# print(df4.columns)
# print(df4['dates'].value_counts())

