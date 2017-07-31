# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 01:28:54 2017

@author: Shabaka
"""

# Import create_engine function
from sqlalchemy import create_engine

# Create an engine to the census database
engine = create_engine('postgresql+psycopg2://' + 'student:datacamp'+\
'@postgresql.csrrinzqubik.us-east-1.rds.amazonaws.com'':5432/census')

# Use the 'table_names()' method on the engine to print the table names
print(engine.table_names())