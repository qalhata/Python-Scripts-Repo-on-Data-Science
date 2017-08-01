# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 03:24:25 2017

@author: Shabaka
"""

# Import packages
import numpy as np
import h5py

# Assign filename: file
file = 'LIGO_data.hdf5'

# Load file: data
data = h5py.File('LIGO_data.hdf5', 'r')

# Print the datatype of the loaded file
print(type(data))

# Print the keys of the file
for key in data.keys():
    print(key)