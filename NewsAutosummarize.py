# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 21:49:22 2017

@author: Shabaka
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 12:15:24 2017

@author: Shabaka
"""


# Exercise based onhttps:''glowingpython.blogspot.in/2014/09/
# text-summarization-with-nl

# nltk - natural lang processing toolkit

# we sue 2 functions from nltk

# sent_tokenize - given a grp of text tokens, tokenize into sentences

# word_tokenize: given grp of text - tokenize into words

import nltk

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

import urllib.request
from bs4 import BeautifulSoup

#####################################################################
# we use defaultdict - if we try to get item with key that does not exist
# it creates a default item and add the key-value pair to the dictionary
# the default item is taken from it's constructor - it takes a function
# that creates a default object
#####################################################################
# instatiate default dict

from collections import defaultdict
######################################################################
# check for punctuation
from string import punctuation
#######################################################################
# another requirement is a function that will return the n largst elements
# in a given list using a python built in fuctionality
######################################################################

from heapq import nlargest
########################################################
# Now we create the class FrequencySummarizer

# This class captures all behaviours we need
# eliminating stopwords
# finding frequency of words in text
# assigning score of importance for words in text
# rank sentences in the text based on freq above


nltk.download('stopwords')
nltk.download('punkt')

#########################################################################


class FrequencySummarizer:

    def _init_(self, min_cut=0.1, max_cut=0.9):
        # identation changes - we are inside the constructor
        # here we set up the behaviour
        # this is called each time an object of feq summ class is
        # created or instantiated
        self._min_cut = min_cut    # self=keyword that reports the variable
        self._max_cut = max_cut
        # we save the val of the 2 parameters passed by assigning them
        # two member variables - the 'self.' prefix identifies them as part
        # of the self argument - using underscore as first char.
        self._stopwords = set(stopwords.words('english') + list(punctuation))
        # this is alist of all common words and punc symols

    # identation changes - we are out of the constructor here
    # This is still the body of the class
    # Defining var here ( outside a member function) but within the class
    # member var becomes STATIC. This means it belongs to the class, and not
    # to any specific individual instance (object) of the class

    def _compute_frequencies(self, word_sent):
        # computes freq of words int he text
        # being a member func, it take the self arg and a list of
        # sentences in a piece of text
        # returns a dictionary where the keys are words in the sentence
        # and values are the freq of those words in the set of sentences
        freq = defaultdict(int)    # dictionary with extended functionality

        # we use a for loop to count the instances/freq of
        # words in our sentences and add them to our defaultdict
        for sentence in word_sent:
            # change in indentation - the following is in the for loop
            for word in word_sent:
                if word not in self._stopwords:
                    freq[word] += 1
                # the two loops above looks at every word in
                # every sentence, keeps track of all instances
                # of that word (freq).
                # We want to do this for all non-stop words

        # Frequency calculations Done. We go on to do 2 things
        # to our list as follows:
        # 1. We normalize the frequencies by dividing  each by the highest freq
        # 2. Filter out frequencies that are too high or too low

        # (1) helps make the frequencies comparable - all freq btw 0 - 1
        # (2) captures almost all srop words (normally very high)
        max_freq = float(max(freq.values()))
        # this gives maximum frequency
        for word in freq.keys():
            # ident change - we are in the for loop
            freq[word] = freq[word]/max_freq
            # 1. this divides the word freq by max freq
            if freq[word] >= self._max_cut or freq[word] <= self._min_cut:
                # inside the conditional
                del freq[word]
                # we us e del to remove key-value pairs from a dict
        return freq
        # the member function is completed - returns the frequency dictionary

    def summarize(self, text, n):
        # we are now goign to define the next member func
        # this member fxn takes in self ( same for any other member func)
        # it takes a raw text input(the article of interest)
        # n is th enumber of sentences we want to return
        sents = sent_tokenize(text)   # splits text into sentences
        assert n <= len(sents)
        # the assert is a way of making sure a condition hold true
        # else, we get an exception - for sanity checks
        # here we assert that the summary is no longer than whole article
        word_sent = [word_tokenize(s.lower()) for s in sents]
        # the line of code above first converts every sentence to lowercase
        # it then splits each sentence into words.
        # it then takes all lists of sentences words as above, and then
        # combines them into one giant list
        self._freq = self._compute_frequencies(word_sent)
        # make a call to the method ( member func) _compute_frequencies
        # that gives in the giant list of words and gets
        # back a dictionary with all frequencies
        ranking = defaultdict(int)
        # this creates an empty dictionary (the defaultdict variety)
        # this holds the ranking of the sentenses int he text.
        for i, sent in enumerate(word_sent):
            # ident - inside the for loop
            # we use a for loop and the built-in fucnt enmerate
            # If we have alist ['a'. 'b', 'c'...] - enumerate outputs a
            # list of tuples[(0,'a'), (1, 'b'), (2, 'c')]
            # enumerate eliminates the need for a counter variable
            # to keep track of hat index of the list is currently on
            # this requires that we have 2 loop variables
            for word in sent:
                # indent into second for loop
                if word is self._freq:
                    ranking[i] += self._freq[word]
                    # the above does the following
                    # for each word in each sentence,
                    # we compute a rank for that sentence as a sum
                    # of the frequencies of the words in that sentence
                    # this ofcourse excludes stop words as spec'd earlier
            # sentences
        sents_idx = nlargest(n, ranking, key=ranking.get)
        # Here we wish to find the first n sentences
        # that have the highest ranking, the 'nlargest' method helps here
        # to fulfill the requirement of knowing how to sort the sentences
        # we pass int he rankings.get method
        return [sents[j] for j in sents_idx]

####################################################################
# Now we get an article from the web URL and summarize it using urllib2
# and BeautifulSoup
#####################################################################

#############################################################
# we define a function that takes  a url of an article and
# return the raw text of the article


def get_only_text_washingtonpost_url(url):
    # this func will take the URL as an argument and return only
    # the raw text of the url.
    # this function works specifically for the washPost articles
    # because we know the structure of the pages
    page = urllib.urlopen(url).read().decode('utf8')
    # we download the URL
    soup = BeautifulSoup(page)
    # initialize a beautifulsoup object with the page we downloaded
    text = ' '.join(map(lambda p: p.text, soup.find_all('article')))
    # the above gets everything bewteen a pair of HTML tags
    # that look a certain way e.g. <article> stuff</article>
    # the above format is specific to the washington post
    soup2 = BeautifulSoup(text)
    # find all the paragraph tage <p>
    text = ' '.join(map(lambda p: p.text, soup2.find_all('p')))
    return soup.title.text, text

#######################################################################

# TEST
######################################################################
someUrl = 'https://www.washingtonpost.com/politics/?utm_term=.9897b28da9af'
textOfUrl = 'https://www.washingtonpost.com/politics/?utm_term=.9897b28da9af'

fs = FrequencySummarizer()
# we instantiate the frequency summarizer class and get an object of this class

summary = fs.summarize(textOfUrl[1], 1)