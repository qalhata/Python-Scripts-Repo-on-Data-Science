# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 12:39:59 2017

@author: Shabaka
"""

import os
import glob
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
# from mayavi import mlab
import multiprocessing
import plotly.plotly as py
import plotly.graph_objs as go
from plotly.graph_objs import Surface


path = r'C:\Users\Shabaka\Desktop\Test2 DJI_Corretti\100\TIM'
# path = r'C:\DRO\DCL_rawdata_files'
allFiles = glob.glob(path + "/*.csv")
# frame = pd.DataFrame()
list_TIM = []
for file_ in allFiles:
    df_TIM = pd.read_csv(file_, index_col=None, header=0)
    list_TIM.append(df_TIM)
frame = pd.concat(list_TIM)   # ignore_index=True)

print(frame.head())

# sns.heatmap(frame.head())

plt.show()

temp = pd.read_csv('C:\\Users\\Shabaka\\Desktop\\Temperatura_Media.csv')
# Plot the aapl time series in blue
print(temp.head())
plt.plot(temp, color='blue', label='Temp_Median..(yr)')

plt.show()


# Plot the pairwise joint distributions grouped by 'origin' along with
# regression lines
# sns.pairplot(temp, kind='reg', hue='Temp_Med')
# plt.show()

# urb_pop_reader = pd.read_csv(filename, chunksize=1000)

"""
files = glob("*.txt")
fig, ax = plt.subplots()

for f in files:
    print("Current file is"+f)
    #your csv loading into data
    data.plot('time','temp',ax=axes[0])

#outside of the for loop
plt.savefig("myplots.png")

"""

# ''''''''''''3D Density MAp Plot ''''''''''#

def calc_kde(data):
    return kde(data.T)

mu, sigma = 0, 0.1
x = 10*np.random.normal(mu, sigma, 5000)
y = 10*np.random.normal(mu, sigma, 5000)
z = 10*np.random.normal(mu, sigma, 5000)

xyz = np.vstack([x, y, z])
kde = stats.gaussian_kde(xyz)

# Evaluate kde on a grid
xmin, ymin, zmin = x.min(), y.min(), z.min()
xmax, ymax, zmax = x.max(), y.max(), z.max()
xi, yi, zi = np.mgrid[xmin:xmax:30j, ymin:ymax:30j, zmin:zmax:30j]
coords = np.vstack([item.ravel() for item in [xi, yi, zi]])

# Multiprocessing
cores = multiprocessing.cpu_count()
pool = multiprocessing.Pool(processes=cores)
results = pool.map(calc_kde, np.array_split(coords.T, 2))
density = np.concatenate(results).reshape(xi.shape)

# Plot scatter with mayavi
figure = mlab.figure('DensityPlot')

grid = mlab.pipeline.scalar_field(xi, yi, zi, density)
min = density.min()
max = density.max()
mlab.pipeline.volume(grid, vmin=min, vmax=min + .5*(max-min))

mlab.axes()
mlab.show()


# '''''''' Alternativc Route'''''''''''''#
filename = 'C:\\Users\\Shabaka\\Desktop\\Temperatura_Media.csv'
raw_data = open(filename, 'rt')
tempdata = pd.read_csv(raw_data, header=0)
print(tempdata.shape)

print(tempdata.head())

plt.plot(tempdata, color='blue', label='Temp_Med')

plt.show()

sns.pairplot(tempdata, kind='reg')    # hue='Temp_Med')
plt.show()

surfdata = [go.Surface(tempdata.as_matrix())]

layout = go.Layout(
    title='Temp_Data Elevation',
    autosize=False,
    width=500,
    height=500,
    margin=dict(
        l=65,
        r=50,
        b=65,
        t=90
    )
)
fig = go.Figure(data=surfdata, layout=layout)
py.iplot(fig, filename='elevations-3d-surface', type='surface')

plt.show()