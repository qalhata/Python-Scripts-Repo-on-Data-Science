# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 00:01:32 2017

@author: Shabaka
"""

# Import packages
import requests
from bs4 import BeautifulSoup

# Specify url: url
url = 'https://www.python.org/~guido/'

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Extract the response as html: html_doc
html_doc = r.text

# Create a BeautifulSoup object from the HTML: soup
soup = BeautifulSoup(html_doc)  # presents page in a readable manner
soup.body.text

bold = soup.finaAll('b')    # find all bold text and return a list

print(bold)
print(soup.prettify())
# Get the title of Guido's webpage: guido_title
guido_title = (soup.title)

# Print the title of Guido's webpage to the shell
print(guido_title)

# Get Guido's text: guido_text
guido_text = (soup.get_text())

# Print Guido's text to the shell
print(guido_text)

soup.findAll(id-"para2")[0].text
soup.findAll(['b', 'p'])

soup.findAll({'b': True, 'p': True})

# find all links in the document

links = soup.find('a')   # retruns 1st match it gets -use findAll

print(links['href'] + " is the url and " + links.text + " is the text")


# Use find in various ways 

# findParents, findNextSiblings, findPreviousSiblings
# findNext, findPrevious and findAllNext and findAllPrevious