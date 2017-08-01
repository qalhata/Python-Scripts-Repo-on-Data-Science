# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 23:03:45 2017

@author: Shabaka
"""

# import pandas
import pandas as pd
# Import Pyplot as plt from matplotlib
import matplotlib.pyplot as plt

from sqlalchemy import create_engine

# Import func
from sqlalchemy.sql import func

from sqlalchemy import MetaData, Table
metadata = MetaData()

engine = create_engine('sqlite:///census_nyc.sqlite')

# Reflect census table from the engine: census
census = Table('census', metadata, autoload=True, autoload_with=engine)

# Build an expression to calculate the sum of pop2008 labeled as population
pop2008_sum = func.sum(census.columns.pop2008).label("population")

# Build a query to select the state and sum of pop2008 as population grouped by
# state: stmt
stmt = select([census.columns.state, pop2008_sum])

# Append group by state
stmt = stmt.group_by(census.columns.state)

# Execute the statement and store all the records: results
results = connection.execute(stmt).fetchall()

# Print results
print(results)

# Print the keys/column names of the results returned
print(results[0].keys())


# Create a DataFrame from the results: df
df = pd.DataFrame(results)

# Set column names
df.columns = results[0].keys()

# Print the Dataframe
print(df)

# Create a DataFrame from the results: df
df = pd.DataFrame(results)

# Set Column names
df.columns = results[0].keys()

# Print the DataFrame
print(df)

# Plot the DataFrame
df.plot.bar()
plt.show()

