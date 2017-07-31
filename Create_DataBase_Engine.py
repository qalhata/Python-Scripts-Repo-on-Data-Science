# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 19:13:40 2017

@author: Shabaka
"""

# Import necessary module
from sqlalchemy import create_engine
import pandas as pd

# Create engine: engine
engine = create_engine('sqlite:///Chinook.sqlite')


# Save the table names to a list: table_names
table_names = engine.table_names()

# Print the table names to the shell
print(table_names)

"""
    Open the engine connection as con using the method connect() on the engine.
    Execute the query that selects ALL columns from the Album table. Store the
    results in rs.
    Store all of your query results in the DataFrame df by applying the 
    fetchall() method to the results rs.
    Close the connection!
"""

# 'Retrieve column of table called Album in the chinook database'

# Open engine connection: con
con = engine.connect()

# Perform query: rs
rs = con.execute('SELECT * FROM Album')

# Save results of the query to DataFrame: df
df = pd.DataFrame(rs.fetchall())
