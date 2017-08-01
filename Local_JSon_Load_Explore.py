# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 00:59:00 2017

@author: Shabaka
"""

# import module
import json

# Load JSON: json_data
with open("a_movie.json") as json_file:
    json_data = json.load(json_file)

# Print each key-value pair in json_data
for k in json_data.keys():
    print(k + ': ', json_data[k])