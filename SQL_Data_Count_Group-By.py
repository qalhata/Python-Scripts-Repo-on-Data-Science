# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 22:15:59 2017

@author: Shabaka
"""

# Import func
from sqlalchemy.sql import func

# Build a query to select the state and count of ages by state: stmt
stmt = select([census.columns.state, func.count(census.columns.age)])

# Append group by state
stmt = stmt.group_by(census.columns.state)

# Execute the statement and store all the records: results
results = connection.execute(stmt).fetchall()

# Print results
print(results)

# Print the keys/column names of the results returned
print(results[0].keys())