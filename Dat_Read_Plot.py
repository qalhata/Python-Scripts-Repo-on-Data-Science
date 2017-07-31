# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 18:57:00 2017

@author: Shabaka
"""

import os
import glob
import pandas as pd
import mayavi
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
from mayavi import mlab
import multiprocessing
import plotly.plotly as py
import plotly.graph_objs as go
from plotly.graph_objs import Surface


path = 'C:\\Users\\Shabaka\Desktop\\Test2 DJI_Corretti'
all_files = glob.glob(os.path.join(path, "*Temperatura_Media.csv"))

df_from_each_file = pd.read_csv(all_files)
conc_df = pd.concat(df_from_each_file, ignore_index=True)

print(conc_df.head())
