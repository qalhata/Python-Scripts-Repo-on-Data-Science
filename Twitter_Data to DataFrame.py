# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 02:54:50 2017

@author: Shabaka
"""

# Import package
import pandas as pd

# Build DataFrame of tweet texts and languages
df = pd.DataFrame(tweets_data, columns=['text', 'lang'])

# Print head of DataFrame
print(df.head())