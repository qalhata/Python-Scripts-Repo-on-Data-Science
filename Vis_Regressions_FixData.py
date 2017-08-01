# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 19:34:27 2017

@author: Shabaka
"""

# Import plotting modules
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# ''''' File Import to panda dataframe '#

fixdat = pd.read_csv('C:\\Users\\Shabaka\\ShabakaCodes\\fixations.csv',
                     index_col=0, parse_dates=True)

fix_chunk = pd.read_csv('C:\\Users\\Shabaka\\ShabakaCodes\\fixations.csv',
                        chunksize=50)

# Plot a linear regression between 'weight' and 'hp'
sns.lmplot(x='duration', y='confidence', data=fixdat)

# Display the plot
plt.show()

# '''''''' Plotting residuals of a regression ''''''#

# Import plotting modules
# import matplotlib.pyplot as plt
# import seaborn as sns

# Generate a green residual plot of the regression between 'hp' and 'mpg'
sns.residplot(x='duration', y='confidence', data=fixdat, color='green')

# Display the plot
plt.show()

# '''''''''' HIgher Order Regressions''''''#

# Generate a scatter plot of 'fix_dur' and 'confidence' using red circles
plt.scatter(fixdat['duration'], fixdat['confidence'],
            label='data', color='red', marker='o')

# Plot in blue a linear regression of order 1 btw 'fix_dur' and 'confidence'
sns.regplot(x='duration', y='confidence', data=fixdat,
            color='blue', label='order 1', scatter=None)

# Plot in green a linear regression of order 2 between 'fixdur' and 'conf'
sns.regplot(x='duration', y='confidence', data=fixdat,
            color='green', label='order 2', scatter=None, order=2)

# Add a legend and display the plot
plt.legend(loc='lower right')
plt.show()


# ''''''''''' Linear Regressions by Hue ''''''''#

# Plot a linear regression between 'duration' and 'confidence', with a hue
# of 'avg pupil size' and palette of 'Set1'
sns.lmplot(x='duration', y='confidence', data=fixdat,
           palette='Set1')    # hue='avg_pupil_size'

# Display the plot

plt.show()

# ''''''''''Strip Plot Construction

# Make a strip plot of 'duration' grouped by 'conf'

plt.subplot(2, 1, 1)
sns.stripplot(x='duration', y='confidence', data=fixdat)

# Make the strip plot again using jitter and a smaller point size
plt.subplot(2, 1, 2)
sns.stripplot(x='duration', y='confidence', data=fixdat, jitter=True, size=3)

# Display the plot
plt.show()

# ''''''''''''''''  Generating Swarmplots '''''''#

# Generate a swarm plot of 'dur' grouped horizontally by 'pupil_size'

plt.subplot(2, 1, 1)
sns.swarmplot(x='avg_pupil_size', y='duration', data=fixdat)

# Gen a swarm plot of 'avgPup_size' grouped vertically
# by 'confidence' with a hue of 'duraton'
plt.subplot(2, 1, 2)
sns.swarmplot(x='avg_pupil_size', y='duration', data=fixdat,
              orient='v')    # hue='confidence')

# Display the plot
plt.show()

# ''''''''''''''' Constructing Violin Plots ''''''''#

# Generate a violin plot of 'avg_pupil_size' grouped horizontally by 'conf'
plt.subplot(2, 1, 1)
sns.violinplot(x='confidence', y='avg_pupil_size', data=fixdat)

# Gen same violin plot: with color= 'lightgray' and without inner annotations
plt.subplot(2, 1, 2)
sns.violinplot(x='confidence', y='avg_pupil_size',
               data=fixdat, inner=None, color='lightgray')

# Overlay a strip plot on the violin plot
sns.stripplot(x='confidence', y='avg_pupil_size',
              data=fixdat, size=1.5, jitter=True)

# Display the plot
plt.show()

# ''''''''''' Plotting Joint Distributions - 1 ''''''''#

# Generate a joint plot of 'fix dur' and 'confidence'
_ = sns.jointplot(x='duration', y='confidence', data=fixdat)

# Display the plot
plt.show()

# Generate a joint plot of 'avg_pupil size and 'duration'
_ = sns.jointplot(x='duration', y='avg_pupil_size', data=fixdat)

# Display the plot
plt.show()


# ''''''''''' Plotting Joint Distributions 2 ''''''''' #

# Hex Bin Plot # - kind = scatter/reg/resid/kde/hex ( as below)

# Generate a joint plot of 'hp' and 'mpg' using a hexbin plot
_ = sns.jointplot(x='duration', y='confidence', data=fixdat, kind='hex')

# Display the plot
plt.show()

# ''''''''''''' Plot the Distibutions Pairwise'''''''''''#

# Print the first 5 rows of the DataFrame
print(fixdat.head())

# Plot the pairwise joint distributions from the DataFrame
sns.pairplot(fixdat)

# Display the plot
plt.show()

# ''''''''' Pairwise Distributtion gropued by origin + reg lines #

# Print the first 5 rows of the DataFrame
print(fixdat.head())

# Plot the pairwise joint distributions grouped by 'origin' along with
# regression lines
sns.pairplot(fixdat, kind='reg', hue='dispersion')

# Display the plot
plt.show()

# ''''''''''' Correlation Viz with a Heat Map - Covariance Matrix)

# Print the covariance matrix
# print(cov_matrix)

# Visualize the covariance matrix using a heatmap
# sns.heatmap(cov_matrix)

# Display the heatmap
# plt.show()

# _ = plt.plot(fixdat)
# _ = plt.legend(loc='upper right')
# _ = plt.show()

