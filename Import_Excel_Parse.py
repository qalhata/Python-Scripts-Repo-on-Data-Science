# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 02:22:12 2017

@author: Shabaka
"""
import pandas as pd
import numpy as np
"""
The spreadsheet 'battledeath.xlsx' is already loaded as xl.

As before, you'll use the method parse(). This time, however, you'll add the
additional arguments skiprows, names and parse_cols. These skip rows, name the
columns and designate which columns to parse, respectively. All these arguments
can be assigned to lists containing the specific row numbers, strings and 
column numbers, respectively.
"""

# Parse the first sheet and rename the columns: df1
df1 = xl.parse(0, skiprows=[0], names=['Country', 'AAM due to War (2002)'])

# Print the head of the DataFrame df1
print(df1.head())

# Parse the first column of the second sheet and rename the column: df2
df2 = xl.parse(1, parse_cols=[0], skiprows=[0], names=['Country'])

# Print the head of the DataFrame df2
print(df2.head())
