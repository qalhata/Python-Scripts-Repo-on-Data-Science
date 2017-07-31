# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 12:18:36 2017

@author: Shabaka
"""

import os
import glob
import pandas as pd


def concatenate(indir='', outfile=''):
    os.chdir(indir)
    fileList = glob.glob('*.csv')
    dfList = []
    
    for filename in fileList:
        print(filename)
        df = pd.read_csv(filename, header=None)
        dfList.append(df)
    concatDF= pd.concat(dfList, axis=0)
    concatDF.columns=colanmes
    concatDF.to_csv
    