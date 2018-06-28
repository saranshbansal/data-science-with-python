# Import necessary module
import pandas as pd
from sqlalchemy import create_engine

from def_path import path

# Create engine: engine
engine = create_engine('sqlite:///' + path + 'Chinook.sqlite')

# Save the table names to a list: table_names
table_names = engine.table_names()

# Print the table names to the shell
print(table_names)

# Open engine connection: con
con = engine.connect()

# Perform query: rs
rs = con.execute('select * from Album')

# Save results of the query to DataFrame: df
df1 = pd.DataFrame(rs.fetchall())

# Close connection
con.close()

# Print head of DataFrame df
print(df1.head())

# ---------------------------------------

# Perform query and save results to DataFrame: df
with engine.connect() as con:
    rs = con.execute('select LastName, Title from Employee')
    df2 = pd.DataFrame(rs.fetchmany(size=3))
    df2.columns = rs.keys()

# Print the length of the DataFrame df
print(len(df2))

# Print the head of the DataFrame df
print(df2.head())

# ---------------------------------------
# Open engine in context manager
# Perform query and save results to DataFrame: df
with engine.connect() as con:
    rs = con.execute('select * from Employee where EmployeeId >= 6')
    df3 = pd.DataFrame(rs.fetchall())
    df3.columns = rs.keys()

# Print the head of the DataFrame df
print(df3.head())
