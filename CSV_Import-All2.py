# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 12:51:39 2017

@author: Shabaka
"""

import os
import glob
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# path = r'C:\DRO\DCL_rawdata_files'

path = r'C:\Users\Shabaka\Desktop\Test2 DJI_Corretti\100\TIM'
allfiles = os.path.join(path, "*.csv")
frame2 = pd.DataFrame()
list2 = []
for file_ in allfiles:
    df = pd.read_csv(file, index_col=None, header=None)
    list2.append(df)
frame = pd.concat(list2, ignore_index=True)

print(frame.head())


df = pd.concat((pd.read_csv(file) for file in allfiles))

print(df.head())