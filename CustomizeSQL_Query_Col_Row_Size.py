# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 14:32:12 2017

@author: Shabaka
"""

"""

    Open the engine connection as con using the method connect() on the engine.
    Execute the query that selects ALL columns from the Album table. Store the
    results in rs.
    Store all of your query results in the DataFrame df by applying the
    fetchall() method to the results rs.
    Close the connection! - In Query Script
"""

# 'This script allows us to perform the following things:'

#    Select specified columns from a table;
#    Select a specified number of rows;
#    Import column names from the database table.


from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('sqlite:///Chinook.sqlite')

# Open engine in context manager
# Perform query and save results to DataFrame: df
with engine.connect() as con:
    rs = con.execute("SELECT LastName, Title FROM Employee")
    df = pd.DataFrame(rs.fetchmany(size=3))
    df.columns = rs.keys()

# Print the length of the DataFrame df
print(len(df))

# Print the head of the DataFrame df
print(df.head())
