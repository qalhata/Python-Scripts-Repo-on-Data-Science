# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 01:22:54 2017

@author: Shabaka
"""

# Import pickle package
import pickle

# Open pickle file and load data: d
with open('data.pkl', 'rb') as file:
    d = pickle.load(file)

# Print d
print(d)

# Print datatype of d
print(type(d))