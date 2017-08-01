# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 14:17:02 2017

@author: Shabaka
"""

class FrequencySummarizer:
    def _init_(self, min_cut=0.1,max_cut=0.9):
        
        self.min_cut = min_cut
        self.max_cut = max_cut
        self._stopwords = set(stopwords.words('english') + list(punctuation) + 
                              [u
# Process 
# 1 - Dload article from url


# 2 - Eliminate stop words etc that add no meaning