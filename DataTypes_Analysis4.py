# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 17:29:54 2017

@author: Shabaka
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re


# Convert the sex column to type 'category'
tips.sex = tips.sex.astype('category')

# Convert the smoker column to type 'category'
tips.smoker = tips.smoker.astype('category')

# Print the info of tips
print(tips.info())

# '''''Working with Numeric Data - Wrong data types ''''#

# Convert 'total_bill' to a numeric dtype
tips['total_bill'] = pd.to_numeric(tips['total_bill'], errors='coerce')

# Convert 'tip' to a numeric dtype
tips['tip'] = pd.to_numeric(tips['tip'], errors='coerce')

# Print the info of tips
print(tips.info())


# '''' String Parsing with regular expression '''#

# Import the regular expression module

# Compile the pattern: prog
prog = re.compile('\d{3}-\d{3}-\d{4}')

# See if the pattern matches
result = prog.match('123-456-7890')
print(bool(result))

# See if the pattern matches
result = prog.match('1123-456-7890')
print(bool(result))

# ''''''' Find Numeric in sstring '''''''' #

# Find the numeric values: matches
matches = re.findall('\d+', 'the recipe requires 10 strawberries and 1 banana')

# Print the matches
print(matches)


# ''''' paTTERN maTCHING '''''##

# Write the first pattern
print(bool(re.match(pattern='\d{3}-\d{3}-\d{4}', string='123-456-7890')))

# Write the second pattern
print(bool(re.match(pattern='\$\d*\.\d{2}', string='$123.45')))

# Write the third pattern
print(bool(re.match(pattern='[A-Z]\w*', string='Australia')))

# '''''''''######## ''''''''''''''''' ##########'''''''''''''''''''#

# '''''Custom Fxn to clean data  in column ( dataframe)''''''''#

# Define recode_sex()


def recode_sex(sex_value):

    # Return 1 if sex_value is 'Male'
    if sex_value == 'Male':
        return 1

    # Return 0 if sex_value is 'Female'
    elif sex_value == 'Female':
        return 0

    # Return np.nan
    else:

        return np.nan


# Apply the function to the sex column
tips['sex_recode'] = tips.sex.apply(recode_sex)


#''' Lambda Functions ''''''#

# Write the lambda function using replace
tips['total_dollar_replace'] = tips.total_dollar.apply(lambda x: x.replace('$', ''))

# Write the lambda function using regular expressions
tips['total_dollar_re'] = tips.total_dollar.apply(lambda x: re.findall('\d+\.\d+', x))

# Print the head of tips
print(tips.head())

# '''''''Dropping DUplicate Data '''''''''''''#

 # Create the new DataFrame: tracks
tracks = billboard[['year', 'artist', 'track', 'time']]

# Print info of tracks
print(tracks.info())

# Drop the duplicates: tracks_no_duplicates
tracks_no_duplicates = tracks.drop_duplicates()

# Print info of tracks
print(tracks_no_duplicates.info())

# '''''''''''''''' Fill in MIssing Data ''''''''' #

# Calculate the mean of the Ozone column: oz_mean
oz_mean = np.mean(airquality.Ozone)

# Replace all the missing values in the Ozone column with the mean
airquality['Ozone'] = airquality['Ozone'].fillna(oz_mean)

# Print the info of airquality
print(airquality.info())

# ''''''''''''''' Data Test with Assert Statements ''''''#

# Assert that there are no missing values
assert pd.notnull(ebola).all().all()

# Assert that all values are >= 0
assert (ebola >= 0).all().all()

# assert pd.notnull(ebola >= 0).all().all()


