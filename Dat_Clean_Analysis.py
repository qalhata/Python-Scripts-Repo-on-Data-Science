# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 02:30:02 2017

@author: Shabaka
"""

# ''Load and View Data ''''''''''#

# Import pandas
import pandas as pd
import matplotlib.pyplot as plt


# Read the file into a DataFrame: df
# df = pd.read_csv('dob_job_application_filings_subset.csv')

df = pd.read_csv('fixations.csv')
df2 = pd.read_csv('aerodata.csv')

# Print the head of df
print(df.head())

# Print the tail of df
print(df.tail())

print('AERO DATA OUTPUT')


print(df2.head())

print(df2.tail())

# Print the shape of df
print(df.shape)

print(df2.shape)

# Print the columns of df
print(df.columns)

print(df2.columns)

# Print the head and tail of df_subset
# print(df.subset.head())
# print(df.subset.tail())

# Print the info of df
print(df.info())

print(df2.info())

# Print the info of df_subset
# print(df.subset.info())


# '''''''' Frequency counts for Categorical Data

# Print the value counts for 'Borough'
print(df['duration'].value_counts(dropna=False))

print(df['duration'].shape)

# Print the value_counts for 'State'
print(df['confidence'].value_counts(dropna=False))

print(df['confidence'].shape)

# Print the value counts for 'Site Fill'
print(df['avg_pupil_size'].value_counts(dropna=False))

# ''''''''''' Single Variable Histogram plot ''''''''#

# Plot the histogram
df['duration'].plot(kind='hist', rot=70, logx=True, logy=True)

# Display the histogram
plt.show()

# ''''' Multi Variable Box Plot Visualisation '''''''#

# Import necessary modules

# Create the boxplot
df.boxplot(column='duration', by='avg_pupil_size', rot=90)

# Display the plot
plt.show()

# ''''''''''' Multiple variable scatter plot visualisation''''#

# Import necessary modules
# import pandas as pd
# import matplotlib.pyplot as plt

# Create and display the first scatter plot
df.plot(kind='scatter', x='initial_cost', y='total_est_fee', rot=70)
plt.show()

# Create and display the second scatter plot
df_subset.plot(kind='scatter', x='initial_cost', y='total_est_fee', rot=70)
plt.show()

