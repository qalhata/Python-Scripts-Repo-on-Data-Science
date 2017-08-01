# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 20:24:53 2017

@author: Shabaka
"""

import numpy as np
import matplotlib.pyplot as plt

# Perform linear regression: a, b
a, b = np.polyfit(x, y, 1)

# Print the slope and intercept
print(a, b)

# Generate theoretical x and y data: x_theor, y_theor
x_theor = np.array([3, 15])
y_theor = a * x_theor + b

# Plot the Anscombe data and theoretical line
_ = plt.plot(x, y, marker='.', linestyle='none')
_ = plt.plot(x_theor, y_theor)

# Label the axes
plt.xlabel('x')
plt.ylabel('y')

# Show the plot
plt.show()

# ########### LINEAR REGRESSION ON ALL DATA ####### ######### #

#### Iterate through x,y pairs
for x, y in zip(anscombe_x, anscombe_y):
    # Compute the slope and intercept: a, b
    a, b = np.polyfit(x, y, 1)

    # Print the result
    print('slope:', a, 'intercept:', b)
    
# ####### BOOTSTRAP VISUALISATION ###  ################# #

for _ in range(50):
    # Generate bootstrap sample: bs_sample
    bs_sample = np.random.choice(rainfall, size=len(rainfall))

    # Compute and plot ECDF from bootstrap sample
    x, y = ecdf(bs_sample)
    _ = plt.plot(x, y, marker='.', linestyle='none',
                 color='gray', alpha=0.1)

# Compute and plot ECDF from original data
x, y = ecdf(rainfall)
_ = plt.plot(x, y, marker='.')

# Make margins and label axes
plt.margins(0.02)
_ = plt.xlabel('yearly rainfall (mm)')
_ = plt.xlabel('ECDF')

# Show the plot
plt.show()

# ###########  BOOTSTRAP  REPLICATE FUNCTION ####### ############ #


# def boostrap_replicate_1d(data, func):

#    bs_sample = np.random.coice(data, len(data))
#    return func(bs_sample)

# ################# ALTERNATIVE FUNCTION ########### #


def boostrap_replicate_1d(data, func):

    """Generate bootstrap replicate of 1D Data"""
    return func(np.random.choice(data, size=len(data)))


# ######## MULTIPLE BOOTSTRAP REPLICATES ######### ######### #

bs_replicates = np.empty(10000)

for i in range(10000):
    bs_replicates[i] = bootstrap_replicate_1d(data, np.mean)
        

