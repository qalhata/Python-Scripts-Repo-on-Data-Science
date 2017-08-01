# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 02:43:07 2017

@author: Shabaka
"""



# Build a list of dictionaries: values_list
values_list = [
    {'name': 'Anna', 'count': 1, 'amount': 1000.00, 'valid':True},
    {'name' : 'Taylor', 'count':1, 'amount':750.00, 'valid':False}
]

# Build an insert statement for the data table: stmt
stmt = insert(data)

# Execute stmt with the values_list: results
results = connection.execute(stmt, values_list)

# Print rowcount
print(results.rowcount)