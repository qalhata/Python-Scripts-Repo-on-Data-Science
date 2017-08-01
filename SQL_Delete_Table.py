# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 23:59:59 2017

@author: Shabaka
"""
import sqlalchemy
# Import delete, select
from sqlalchemy import delete, select

# Build a statement to empty the census table: stmt
stmt = delete(census)

# Execute the statement: results
results = connection.execute(stmt)

# Print affected rowcount
print(results.rowcount)

# Build a statement to select all records from the census table

stmt = select([census])

# Print the results of executing the statement to verify
# there are no rows

print(connection.execute(stmt).fetchall())

# ##################### ################ ################ ########
# '''''' Deleting Specific records '''''''##

# Build a statement to count records using
# the sex column for Men ('M') age 36: stmt

stmt = select([func.count(census.columns.sex)]).where(
    and_(census.columns.sex == 'M',
         census.columns.age == 36)
)

# Execute the select statement and use the scalar() fetch
# method to save the record count

to_delete = connection.execute(stmt).scalar()

# Build a statement to delete records from the census table: stmt_del

stmt_del = delete(census).where(stmt)

# Append a where clause to target Men ('M') age 36

stmt_del = stmt_del.where(
    and_(census.columns.sex == 'M',
         census.columns.age == 36)
)

# Execute the statement: results
results = connection.execute(stmt_del)

# Print affected rowcount and to_delete record count, make sure they match
print(results.rowcount, to_delete)


# '''''''' Delete TAble COmpletely ''''''''''#

# Drop the state_fact table
state_fact.drop(engine)

# Check to see if state_fact exists
print(state_fact.exists(engine))

# Drop all tables
metadata.drop_all(engine)

# Check to see if census exists
print(census.exists(engine))