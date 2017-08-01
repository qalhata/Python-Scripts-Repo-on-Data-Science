# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 00:24:52 2017

@author: Shabaka
"""

import numpy as  np
import pandas as pd

data = np.genfromtxt('gaze_positions.csv', delimiter=',', names=True, dtype=None)

np.shape(data)


data[0]


#More mixed datatypes

# Assign the filename: file
file = 'titanic.csv'

# Import file using np.recfromcsv: d
d = np.recfromcsv(file)

#np.recfrocsv already contains the default 
#delimiter as a comma and dtype is none

# Print out first three entries of d
print(d[:3])