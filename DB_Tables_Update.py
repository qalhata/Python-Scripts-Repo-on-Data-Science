# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 17:05:28 2017

@author: Shabaka
"""

# '''''''''''' Panda SQL Query ''''''''''''#
# Import packages
import sqlite3 
from sqlalchemy import create_engine
from sqlalchemy import update
from sqlalchemy import connection
import pandas as pd
# Import insert and select from sqlalchemy
from sqlalchemy import insert, select
# Create engine: engine
engine = create_engine('sqlite:///Chinook.sqlite')

# Execute query and store records in DataFrame: df
df = pd.read_sql_query("SELECT * FROM Album", engine)

# Print head of DataFrame

print(df.head())

# Open engine in context manager
# Perform query and save results to DataFrame: df1

with engine.connect() as con:
    rs = con.execute("SELECT * FROM Album")
    df1 = pd.DataFrame(rs.fetchall())
    df1.columns = rs.keys()

# Confirm that both methods yield the same result: does df = df1 ?

print(df.equals(df1))

# ''''''''''''#######'''''''##################''''''''#

# Build an insert statement to insert a record into the data table: stmt

stmt = insert(data).values(name='Anna', count=1, amount=1000.00, valid=True)

# Execute the statement via the connection: results

results = connection.execute(stmt)

# Print result rowcount

print(results.rowcount)

# Build a select statement to validate the insert

stmt = select([data]).where(data.columns.name == 'Anna')

# Print the result of executing the query.

print(connection.execute(stmt).first())

# '''''''''###########'''''''''''''''' #
# ''''''####'''''''''''''##########'''''''''#

# Create a insert statement for census: stmt

stmt = insert(census)

# Create an empty list and zeroed row count: values_list, total_rowcount

values_list = []
total_rowcount = 0

# Enumerate the rows of csv_reader
for idx, row in enumerate(csv_reader):
    # create data and append to values_list
    data = {'state': row[0], 'sex': row[1], 'age': row[2], 'pop2000': row[3],
            'pop2008': row[4]}
    values_list.append(data)

    # Check to see if divisible by 51
    if idx % 51 == 0:
        results = connection.execute(stmt, values_list)
        total_rowcount += results.rowcount
        values_list = []
        

# Build a select statement: select_stmt
select_stmt = select([state_fact]).where(state_fact.columns.name == 'New York')

# Print the results of executing the select_stmt
print(connection.execute(select_stmt).fetchall())

# Build a statement to update the fips_state to 36: stmt
stmt = update(state_fact).values(fips_state=36)

# Append a where clause to limit it to records for New York state
stmt = stmt.where(state_fact.columns.name == 'New York')

# Execute the statement: results
results = connection.execute(stmt)

# Print rowcount
print(results.rowcount)

# Execute the select_stmt again to view the changes
print(connection.execute(select_stmt).fetchall())


# ''''''''''''' Update Multiple Records ''''''#

# Build a statement to update the notes to 'The Wild West': stmt
stmt = update(state_fact).values(notes='The Wild West')

# Append a where clause to match the West census region records
stmt = stmt.where(state_fact.columns.census_region_name == 'West')

# Execute the statement: results
results = connection.execute(stmt)

# Print rowcount
print(results.rowcount)

# ''''''''''' Making Correlated Updates ''' ########

# Build a statement to select name from state_fact: stmt
fips_stmt = select([state_fact.columns.name])

# Append a where clause to Match the fips_state to flat_census fips_code
fips_stmt = fips_stmt.where(
    state_fact.columns.fips_state == flat_census.columns.fips_code)

# Build an update statement to set the name to fips_stmt: update_stmt
update_stmt = update(flat_census).values(state_name=fips_stmt)

# Execute update_stmt: results
results = connection.execute(update_stmt)

# Print rowcount
print(results.rowcount)


