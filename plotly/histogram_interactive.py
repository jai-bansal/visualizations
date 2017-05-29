# This script creates an interactive histogram using 'census_data.csv'.

# A description of 'census_data.csv' can be found in 'census_data_scrape_and_process.R'.

################
# IMPORT MODULES
################

# Import modules.
import os
import pandas as pd
import numpy as np
import plotly
from plotly.graph_objs import Histogram, Scatter, Layout

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

# Create data subset consisting of all 2010 observations.
census_subset = census_data[['Name', '2010']]

# Remove row containing total population of United States.
census_subset = census_subset[census_subset['Name'] != 'United States']

# Divide population values by 1000000 for easier graph viewing.
census_subset['2010'] = census_subset['2010'] / 1000000

###########
# PLOT DATA
###########

# Add histogram data.
histogram = Histogram(x = census_subset['2010'],
                      autobinx = False,
                      xbins = dict(start = 0,
                                   end = 40,
                                   size = 3))

# Add layout (with annotations).
# The annotations are done more manually than I'd like...
layout = Layout(title = 'Frequency of 2010 US State Populations (in millions)',
                xaxis = dict(title = '2010 Populations (in millions)'),
                yaxis = dict(title = 'Frequency'),
                font = dict(size = 20),
                annotations = [dict(x = 24.5,
                                    y = 2.5,
                                    text = 'Texas',
                                    showarrow = False),
                               dict(x = 25,
                                    y = 1,
                                    text = '25.15M',
                                    showarrow = True),  
                               dict(x = 37,
                                    y = 2.5,
                                    text = 'California',
                                    showarrow = False),
                               dict(x = 37,
                                    y = 1,
                                    text = '37.25M',
                                    showarrow = True)])

# Plot data.
histogram_data = [histogram,]
plotly.offline.plot(dict(data = histogram_data,
                         layout = layout))








