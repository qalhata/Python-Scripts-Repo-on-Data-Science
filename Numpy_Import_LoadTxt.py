# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 12:51:35 2017

@author: Shabaka
"""

# Import numpy
import numpy as np

# Assign the filename: file
file = 'digits_header.txt'

# Load the data: data
data = np.loadtxt(file, delimiter='\t', skiprows= 1, usecols= [0,2])

# Print data
print(data)