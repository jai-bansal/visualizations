# This script creates an interactive bar graph using 'census_data.csv'.

# A description of 'census_data.csv' can be found in 'census_data_scrape_and_process.R'.

################
# IMPORT MODULES
################

# Import modules.
import os
import pandas as pd
import numpy as np
import plotly
import plotly.graph_objs as pgo

#############
# IMPORT DATA
#############

# Set working directory.
# This obviously needs to be changed depending on the computer being used.
os.chdir('D:\\Users\\JBansal\\Documents\\GitHub\\visualizations')

# Load data.
census_data = pd.read_csv('census_data.csv',
                          encoding = 'latin-1')

################
# TRANSFORM DATA
################

# Specify states of interest.
states = ['Delaware', 'Maryland', 'New Jersey', 'Pennsylvania', 'Virginia', 'West Virginia']

# Create data subset.
census_subset = census_data[census_data['Name'].isin(states)]
census_subset = census_subset[['Name', '2010']]

# Reset 'census_subset' index.
census_subset.reset_index(drop = True,
                          inplace = True)

# Divide population values by 1000000 for easier graph viewing.
census_subset['2010'] = census_subset['2010'] / 1000000

###########
# PLOT DATA
###########

plotly.offline.plot({
    "data": [
        pgo.Bar(
            x = census_subset['Name'],
            y = census_subset['2010'])],
    "layout": pgo.Layout(title = 'Selected State Populations in 2010 (in thousands)',
                         xaxis = dict(
                             title = 'State'),
                         yaxis = dict(
                             title = '2010 Population (thousands)'))
    })

        
