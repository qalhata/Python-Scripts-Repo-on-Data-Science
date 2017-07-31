# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 01:37:31 2017

@author: Shabaka
"""

# Import requests package
import requests

# Assign URL to variable: url
url = 'http://www.omdbapi.com/?t=this+is+spinal+tap'

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Print the text of the response
print(r.text)