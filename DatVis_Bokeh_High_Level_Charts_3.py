# -*- coding: utf-8 -*-
"""
Created on Wed May 17 19:35:15 2017

@author: Shabaka
"""
import pandas as pd
import numpy as np

from bokeh.plotting import figure
from bokeh.io import output_file, show
from bokeh.plotting import ColumnDataSource
from bokeh.models import HoverTool
from bokeh.layouts import gridplot
from bokeh.models.widgets import Panel
from bokeh.models.widgets import Tabs
from bokeh.layouts import row, column
from bokeh.charts import BoxPlot
from bokeh.charts import Scatter

# Import Histogram, output_file, and show from bokeh.charts
from bokeh.charts import Histogram


# ''''' Basic bokeh Histogram ''''''''#
df = pd.read_csv('fixations.csv')

df.head()

# Create a ColumnDataSource from df: source
source = ColumnDataSource(df)

# Make a Histogram: p
p = Histogram(df, 'duration', title='Gaze_Time', bins=50)

# Set the x axis label
p.xaxis.axis_label = 'Gaze_Duration'

# Set the y axis label
p.yaxis.axis_label = 'Pupil DIa'
# Specify the name of the output_file and show the result
output_file('histogram.html')
show(p)

"""
# Make a Histogram: p
p = Histogram(df, 'female_literacy', title='Female Literacy',
              bins=40)

# Set the x axis label
p.xaxis.axis_label = 'Female Literacy'

# Set the y axis label
p.yaxis.axis_label = 'Fertility'
# Specify the name of the output_file and show the result
output_file('histogram.html')
show(p)

"""
# '''''' Multiple Histograms ''''''''#

# Make a Histogram: p
p = Histogram(df, 'female_literacy', title='Female Literacy',
              color='Continent', legend='top_left')

# Set axis labels
p.xaxis.axis_label = 'Female Literacy (% population)'
p.yaxis.axis_label = 'Number of Countries'

# Specify the name of the output_file and show the result
output_file('hist_bins.html')

"""
# '''''' Basic BoxPlot '''''''''#

# Make a box plot: p
p = BoxPlot(df, values='duration', label='confidence',
            title='Gaze Duration (grouped by Avg_Pupil_Size)',
            legend='bottom_right')

# Set the y axis label
p.yaxis.axis_label = 'Fixations (% Tot_Gaze_Pop)'

# Specify the name of the output_file and show the result
output_file('boxplot.html')
show(p)
"""

# ''''''''''''''' ################ '''''''''''''' #
# Make a box plot: p
p = BoxPlot(df, values='female_literacy', label='Continent',
            title='Female Literacy (grouped by Continent)',
            legend='bottom_right')

# Set the y axis label
p.yaxis.axis_label = 'Female literacy (% population)'

# Specify the name of the output_file and show the result
output_file('boxplot.html')
show(p)

# ''''''''''' Multicoloured Boxplots ''''''#

# Make a box plot: p
p = BoxPlot(df, values='female_literacy',
            label='Continent', color='Continent',
            title='Female Literacy (grouped by Continent)',
            legend='bottom_right')

# Set y-axis label
p.yaxis.axis_label = 'Female literacy (% population)'

# Specify the name of the output_file and show the result
output_file('boxplot.html')
show(p)

# ''''''''' Basic Bokeh Scatter PLot ''''''#

# Make a scatter plot: p
p = Scatter(df, x='population', y='female_literacy',
            title='Female Literacy vs Population')

# Set the x-axis label
p.xaxis.axis_label = 'Population'

# Set the y-axis label
p.yaxis.axis_label = 'Female Literacy'
# Specify the name of the output_file and show the result
output_file('scatterplot.html')
show(p)

# ''''' scatter plot grouping by colour ''''#

# Make a scatter plot such that each circle
# is colored by its continent: p
p = Scatter(df, x='population', y='female_literacy',
            color='Continent',
            title='Female Literacy vs Population')

# Set x-axis and y-axis labels
p.xaxis.axis_label = 'Population (millions)'
p.yaxis.axis_label = 'Female literacy (% population)'

# Specify the name of the output_file and show the result
output_file('scatterplot.html')

# ''''' Scatter plot shape(marker) grouping '''''#

# Make a scatter plot such that each continent has a different marker type: p
p = p = Scatter(df, x='population', y='female_literacy',
                color='Continent',
                marker='Continent',
                title='Female Literacy vs Population')

# Set x-axis and y-axis labels
p.xaxis.axis_label = 'Population (millions)'
p.yaxis.axis_label = 'Female literacy (% population)'

# Specify the name of the output_file and show the result
output_file('scatterplot.html')
show(p)

