# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 13:15:13 2017

@author: Shabaka
"""

# import and_
from sqlalchemy import and_

# BUild a query for the census table: stmt
stmt = select([census])

# Append a where clause to select only non-male records from California using and_

stmt = stmt.where(
    # The state of California with a non-male sex                  
     and_(census.columns.state == 'California', census.columns.sex != 'M')
             
                  )

# Loop over the ResultProxy printing the age and sex
for result in connection.execute(stmt):
    print(result.age, result.sex)
    
    