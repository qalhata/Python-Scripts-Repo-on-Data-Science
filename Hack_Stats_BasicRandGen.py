# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 21:05:24 2017

@author: Shabaka
"""

import numpy as np
import matplotlib.pyplot as plt

# Seed the random number generator
np.random.seed(42)

# Initialize random numbers: random_numbers
random_numbers = np.empty(100000)

# Generate random numbers by looping over range(100000)
for i in range(100000):
    random_numbers[i] = np.random.random()

# Plot a histogram
_ = plt.hist(random_numbers)

# Show the plot
plt.show()
