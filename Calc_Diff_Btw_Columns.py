# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 02:16:54 2017

@author: Shabaka
"""

from sqlalchemy import desc

# Build query to return state names by population difference from 2008 to 2000:
# stmt
stmt = select([census.columns.state, (census.columns.pop2008 -census.columns.pop2000).label('pop_change')])

# Append group by for the state: stmt
stmt = stmt.group_by(census.columns.state)

# Append order by for pop_change descendingly: stmt
stmt = stmt.order_by(desc('pop_change'))

# Return only 5 results: stmt
stmt = stmt.limit(5)

# Use connection to execute the statement and fetch all results
results = connection.execute(stmt).fetchall()

# Print the state and population change for each record
for result in results:
    print('{}-{}'.format(result.state, result.pop_change))
