# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 17:34:53 2017

@author: Shabaka
"""

# Build a query to select the state column: stmt
stmt = select([census.columns.state])

# Append an order_by state
stmt = stmt.order_by(census.columns.state)

# Execute the query and store the results: results
results = connection.execute(stmt).fetchall()

# Print the first 10 results
print(results[:10])