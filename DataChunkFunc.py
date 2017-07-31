# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 13:19:38 2017

@author: Shabaka
"""

import pandas as pd
import matplotlib.pyplot as plt

# Define plot_pop()
def plot_pop(filename, country_code):

    # Initialize reader object: urb_pop_reader
    urb_pop_reader = pd.read_csv(filename, chunksize=1000)

    # Initialize empty dataframe: data
    data = pd.DataFrame()

    # Iterate over each dataframe chunk
    for df_urb_pop in urb_pop_reader:
        # Check out specific country: df_pop_ceb
        df_pop_ceb = df_urb_pop[df_urb_pop['CountryCode'] == country_code]

        # Zip dataframe columns of interest: pops
        pops = zip(df_pop_ceb['Total Population'],
                   df_pop_ceb['Urban population (% of total)'])

        # Turn zip object into list: pops_list
        pops_list = list(pops)

        # Use list comprehension to create new
        # dataframe column 'Total Urban Population'
        df_pop_ceb['Total Urban Population'] = \
                  [int(tup[0] * tup[1]) for tup in pops_list]

        # Append dataframe chunk to data: data
        data = data.append(df_pop_ceb)

    # Plot urban population data
    data.plot(kind='scatter', x='Year', y='Total Urban Population')
    plt.show()