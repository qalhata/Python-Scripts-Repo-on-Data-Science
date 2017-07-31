# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 01:21:36 2017

@author: Shabaka
"""

# Select retweets from the Twitter dataframe: result
result = filter(lambda x:x[0:2] == 'RT', tweets_df['text'])

# Create list from filter object result: res_list
res_list = list(result)

# Print all retweets in res_list
for tweet in res_list:
    print(tweet)