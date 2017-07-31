# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 15:03:52 2017

@author: Shabaka
"""

# Import pandas as pd
import pandas as pd

# Assign the filename: file
file = 'titanic.csv'

# Read the file into a DataFrame: df
df = pd.read_csv(file)

# View the head of the DataFrame

print(df.head())

# Assign the filename: file
file = 'digits.csv'

# Read the first 5 rows of the file into a DataFrame: data
data = pd.read_csv(file, nrows=5, header=None)

# Build a numpy array from the DataFrame: data_array
data_array = np.array(data.values)

# Print the datatype of data_array to the shell
print(type(data_array))