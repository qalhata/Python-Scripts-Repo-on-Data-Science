# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 15:03:52 2017

@author: Shabaka
"""

# Import pandas as pd
import pandas as pd

# Assign the filename: file
file = 'fixations.csv'
file2 = 'gaze_postions.csv'

# Read the file into a DataFrame: df
df = pd.read_csv(file)
df2 = pd.read_csv(file2)

# View the head of the DataFrame

print(df.head())
print(df2.head())
