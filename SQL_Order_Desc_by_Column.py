# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 17:50:29 2017

@author: Shabaka
"""

# Import desc
from sqlalchemy import desc
from sqlalchemy import Table, MetaData

# Build a query to select the state column: stmt
stmt = select([census.columns.state])

# Append order_by descending state: rev_stmt
rev_stmt = stmt.order_by(desc(census.columns.state))

# Execute the query and store the results: rev_results
rev_results = connection.execute(rev_stmt).fetchall()

# Print the first 10 rev_results
print(rev_results[:10])