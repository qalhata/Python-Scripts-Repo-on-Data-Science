# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 15:01:21 2017

@author: Shabaka
"""

import pandas as pd
from sqlalchemy import create_engine
"""
Let's say, for example that you wanted to get all records from the Customer 
table of the Chinook database for which the Country is 'Canada'. 
You can do this very easily in SQL
 using a SELECT statement followed by a WHERE clause as follows:

SELECT * FROM Customer WHERE Country = 'Canada'

In fact, you can filter any SELECT statement by any condition using a WHERE
clause. This is called filtering your records.
Below, you'll select all records of the Employee table for which 'EmployeeId'
is greater than or equal to 6
"""

# Create engine: engine
engine = create_engine('sqlite:///Chinnok.sqlite')

# Open engine in context manager
# Perform query and save results to DataFrame: df
with engine.connect() as con:
    rs = con.execute("SELECT * FROM Employee WHERE EmployeeId >= 6")
    df = pd.DataFrame(rs.fetchall())
    df.columns = rs.keys()

# Print the head of the DataFrame df
print(df.head())
