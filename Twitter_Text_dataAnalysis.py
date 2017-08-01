# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 02:56:45 2017

@author: Shabaka
"""

import re
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


def word_in_text(word, tweet):
    word = word.lower()
    text = tweet.lower()
    match = re.search(word, tweet)

    if match:
        return True
    return False

# Build DataFrame of tweet texts and languages
df = pd.DataFrame(tweets_data, columns=['text', 'lang'])

# Print head of DataFrame
print(df.head())
"""
 iterate over the rows of the DataFrame and calculate how many tweets contain
 each of our keywords! The list of objects for each candidate has been
 initialized to 0
"""
# Initialize list to store tweet counts
[clinton, trump, sanders, cruz] = [0, 0, 0, 0]

# Iterate through df, counting the number of tweets in which
# each candidate is mentioned
for index, row in df.iterrows():
    clinton += word_in_text('clinton', row['text'])
    trump += word_in_text('trump', row['text'])
    sanders += word_in_text('sanders', row['text'])
    cruz += word_in_text('cruz', row['text'])


# first import seaborn as sns; you'll then construct a barplot of the
# data using sns.barplot, passing it two arguments: (i) a list of labels and
# (ii) a list containing e variables you wish to plot(clinton, trump and so on)

# Import packages


# Set seaborn style
sns.set(color_codes=True)

# Create a list of labels:cd
cd = ['clinton', 'trump', 'sanders', 'cruz']

# Plot histogram
ax = sns.barplot(cd, [clinton, trump, sanders, cruz])
ax.set(ylabel="count")
plt.show()
