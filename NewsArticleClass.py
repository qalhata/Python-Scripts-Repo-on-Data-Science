# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 23:02:20 2017

@author: Shabaka
"""

import nltk

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import requests
import urllib
import urllib3
from math import log
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from bs4 import BeautifulSoup
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

nltk.download('stopwords')
nltk.download('punkt')

# ########################## Objectives #############################

# We are trying to classify nerws articles on a website
# into tech relaed andnon tech related articles

# 1. We create a corpus of news articles which are
# already labeled as tech and non-tech - dowlaod all tech articles
# and label them as tech. Dload all sports articles and label them
# as non tech articles ( this involves parsing HTML to remove all tags)

# 2. Get problem instance from a blog/article that needs classification

# 3. We use the naive bayes classifier algorithm
# to classify instances as either tech or non-tech
########################################################################
# We define functions to parse and dload contents of URLs from std sources
# with BeautifulSoup


def getWashPostText(url, token):
    # this function takes the url of article and returns article
    # minus the crud - HTML, jabascript etc.
    try:
        page = urllib3.PoolManager.urlopen(url).read().decode('utf8')
    except:
        # here we say if unable to dload url, return title=None;article=None
        return (None, None)
    soup = BeautifulSoup(page)
    if soup is None:
        return (None, None)
    # we say here, the error checks are succesful, page was parsed
    text = ""
    if soup.find_all(token) is not None:
        # here we search the page for tokens which demarcate the article
        # usually '<article></article>'
        text = ''.join(map(lambda p: p.text, soup.find_all(token)))
        soup2 = BeautifulSoup(text)
        if soup2.find_all('p') is not None:
            text = ''.join(map(lambda p: p.text, soup2.find_all('p')))
    return text, soup.title.text


def getNYTText(url, token):
    response = requests.get(url)
    # above line is simply an alternative way to get URL contents
    soup = BeautifulSoup(response.content)
    page = str(soup)
    title = soup.find('title').text
    mydivs = soup.findAll("p", {"class": "story-body-text story-content"})
    text = ''.join(map(lambda p: p.text, mydivs))
    return text, title
    
#######################################################################
# Now we take the above functions which extract title and
# contents of indiv urls, we can now link that up to 
# another function that will take thr url of entire sections
# of the paper - for instance Tech or Sports sections
# and parse all URLs for articles linked off that section
# We also want to filter out all non-news link - so we hack a little
# we go with the logic that articles will have a date in the url
#######################################################################


def scrapeSource(url, magicFrag='2017',
                 scraperFunction=getNYTText, token='None'):
    urlBodies = {}
    requests = urllib3.PoolManager()
    response = requests.request('GET', url)
    soup = BeautifulSoup(response.data)
    # the above lines of code sets up the beautifulSoup page
    # now we find links
    # links are always of the form <a href='url'> link-text </a>
    for a in soup.findAll('a'):
        try:
            # the line above refers to indiv. scrapperFunction
            # for NYT & washPost
            if body and len(body) > 0:
                urlBodies[url] = body
                print(url)
        except:
            numErrors = 0
            numErrors += 1


class FrequencySummarizer:
    def _init_(self, min_cut=0.1, max_cut=0.9):
        self._min_cut = min_cut    # self=keyword that reports the variable
        self._max_cut = max_cut
        self._stopwords = set(stopwords.words('english') +
                              list(punctuation) + [u"'s", '"'])
        # this is alist of all common words and punc symols

    def _compute_frequencies(self, word_sent, customStopWords=None):
        freq = defaultdict(int)
        if customStopWords is None:
            stopwords = set(self._stopwords)
        else:
            stopwords = set(customStopWords).union(self._stopwords)
        for sentence in word_sent:
            # change in indentation - the following is in the for loop
            for word in sentence:
                if word not in stopwords:
                    freq[word] += 1

        m = float(max(freq.values()))
        # this gives maximum frequency
        for word in freq.keys():
            # ident change - we are in the for loop
            freq[word] = freq[word]/m
            # 1. this divides the word freq by max freq
            if freq[word] >= self._max_cut or freq[word] <= self._min_cut:
                # inside the conditional
                del freq[word]
                # we us e del to remove key-value pairs from a dict
        return freq
        # the member function is completed - returns the frequency dictionary

    def extractFeatures(self, article, n, customStopWords=None):
        # pass in article as a tuple ( text, title)
        text = article[0]
        # extract the text
        title = article[1]
        # extract the title
        sentences = sent_tokenize(text)
        # split text into sentences
        word_sent = [word_tokenize(sentences.lower()) for a in sentences]
        # split sentences into words
        self._freq = self._compute_frequencies(word_sent, customStopWords)
        # calculate word freq using member func created above
        if n < 0:
            # how many features (words) to return - a -ve number means
            # no feature ( word) selection, just return all features
            return nlargest(len(self._freq_keys()),
                            self._freq, key=self._freq.get)
        else:
            # here we say if calling e func has asked for a subset
            # then return only the 'n' largest features, i.e. the
            # most important words ( important == frequent, less stopwords)
            return nlargest(n, self._freq, key=self._freq.get)

    def extractRawFrequencies(self, article):
        # this method is similar to above but returns
        # the raw freq.cies ( all word count)
        text = article[0]
        text = article[1]
        sentences = sent_tokenize(text)
        word_sent = [word_tokenize(s.lower()) for s in sentences]
        freq = defaultdict(int)
        for s in word_sent:
            for word in s:
                if word not in self._stopwords:
                    freq[word] += 1
        return freq

    def summarize(self, article, n):
        text = article[0]
        text = article[1]
        sentences = sent_tokenize(text)
        word_sent = [word_tokenize(s.lower()) for s in sentences]
        self._freq = self._compute_frequencies(word_sent)
        ranking = defaultdict(int)
        for i, sentence in enumerate(word_sent):
            for word in sentence:
                if word in self._freq:
                    ranking[i] += self._freq[word]
        sentences_index = nlargest(n, ranking, key=ranking.get)
        return [sentences[j] for j in sentences_index]

##############################################################################
# TEST

urlWashPostNonTech = "https://www.washingtonpost.com/sports"
urlNYTimesNonTech = "https://www.nytimes.com/pages/sports/index.html"

urlWashPostTech = "https://www.washingtonpost.com/business/technology"
urlNYTimesTech = "https://www.nytimes.com/pages/technology/index.html"
#############################################################################

washPostTechArticles = scrapeSource(urlWashPostTech, '2016',
                                    getWashPostText, 'article')

washPostNonTechArticles = scrapeSource(urlWashPostNonTech, '2016',
                                       getWashPostText, 'article')

newYorkTimesTechArticles = scrapeSource(urlNYTimesTech, '2016',
                                        getNYTText, 'None')

newYorkTimesNonTechArticles = scrapeSource(urlNYTimesNonTech, '2016',
                                           getNYTText, 'None')

############################################################################
# collect articles in an easy to summarize form

articleSummaries = {}

for techUrlDictionary in [newYorkTimesTechArticles, washPostTechArticles]:
    for articleUrl in techUrlDictionary:
        if len(techUrlDictionary[articleUrl][0]) > 0:
            fs = FrequencySummarizer()
            summary = fs.extractFeatures(techUrlDictionary[articleUrl], 25)
            articleSummaries[articleUrl] = {'feature-vector': summary,
                                            'label': 'Tech'}
#############################################################################

for nontechUrlDictionary in [newYorkTimesNonTechArticles,
                             washPostNonTechArticles]:
    for articleUrl in nontechUrlDictionary:
        if len(nontechUrlDictionary[articleUrl][0]) > 0:
            fs = FrequencySummarizer()
            summary = fs.extractFeatures(nontechUrlDictionary[articleUrl], 25)
            articleSummaries[articleUrl] = {'feature-vector': summary,
                                            'label': 'Non-Tech'}

# training data all set up
##############################################################################

# We call a test instance


def getDoxyDonkeyText(testUrl, token):
    response = requests.get(url)
    soup = BeautifulSoup(response.content)
    page = str(soup)
    title = soup.find("title").text
    mydivs = soup.findAll("div", {"class": token})
    text = ''.join(map(lambda p: p.text, mydivs))
    return text, title

testUrl = "http://doxydonkey.blospot.in"
testArticle = getDoxyDonkeyText(testUrl, "post-body")

fs = FrequencySummarizer()
testArticleSummary = fs.extractFeatures(testArticle, 25)

####################################################################
# Now we classify the article using the K-Nearest Neigbours
# Gvven some training articles, is the test article a tech article
# or a non-tech article

# We find the 5 nearest articles, and carry out a majority vote
# of those 5 articles - k-nearest algorithm applied
# here to a classification problem
###################################################################
similarities = {}
for articleUrl in articleSummaries:
    oneArticleSummary = articleSummaries[articleUrl]['feature-vector']
    similarities[articleUrl] = len(set(testArticleSummary).intersection(set(oneArticleSummary)))

labels = defaultdict(int)
knn = nlargest(5, similarities, key=similarities.get)
for oneNeighbor in knn:
    labels[articleSummaries[oneNeighbor]['label']] += 1

nlargest(1, labels, key=labels.get)

###############################################################
# Same Classification Problem with Naive Bayes - Requires we know
# the probability distribution of the words in each article

cumulativeRawFrequencies = {'Tech': defaultdict(int), 'Non-Tech': defaultdict(int)}
trainingData = {'Tech': newYorkTimesTechArticles, 'Non-Tech': newYorkTimesNonTechArticles}
for label in trainingData:
    for articleUrl in trainingData[label]:
       if len(trainingData[label][articleUrl][0]) > 0:
           fs = FrequencySummarizer()
           rawFrequencies = fs.extractRawFrequencies(trainingData[label][articleUrl])
           for word in rawFrequencies:
               cumulativeRawFrequencies[label][word] += rawFrequencies[word]

techiness = 1.0
nontechiness = 1.0

for word in testArticleSummary:
    # here we say for each feaature of the test instance
    if word in cumulativeRawFrequencies['Tech']:
        techiness *= 1e3*cumulativeRawFrequencies['Tech'][word] /float(sum(cumulativeRawFrequencies['Tech'].values()))
        # we multiply techiness by prob of the word
        # appearing in the tech article (based on training data)
    else:
        techiness /= 1e3
        # IMPORTANT! - if the word does not appear in the 
        # tech articles of the training data at all,
        # we could simply set that probability to zero
    if word in cumulativeRawFrequencies['Non-Tech']:
        nontechiness *= 1e3*cumulativeRawFrequencies['Non-Tech'][word]/float(sum(cumulativeRawFrequencies['Tech'].values()))
        # we multiply techiness by prob of the word
        # appearing in the tech article (based on training data)
    else:
        nontechiness /= 1e3

###########################################################
# we now scale the level of techiness and vice-versa
# by overall probabilities of techiness and non-techiness
# number of words in all articles (tech and non tech)
# as a proportion of total number of words
############################################################
techiness *= float(sum(cumulativeRawFrequencies['Tech'].values())) / (float(sum(cumulativeRawFrequencies['Tech'].values())) + float(sum(cumulativeRawFrequencies['Non-Tech'].values())))

nontechiness *= float(sum(cumulativeRawFrequencies['Non-Tech'].values())) / (float(sum(cumulativeRawFrequencies['Tech'].values())) + float(sum(cumulativeRawFrequencies['Non-Tech'].values())))

if techiness > nontechiness:
    label = 'Tech'
else:
    label = 'Non-Tech'

print(label, techiness, nontechiness)