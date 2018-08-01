# Import necessary module
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

# Print head of DataFrame
print(df1.head())
print(df2.head())
print(df3.head())
print(df4.head())
