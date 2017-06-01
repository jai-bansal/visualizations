# This script creates an interactive boxplot using 'census_data.csv'.

################
# IMPORT MODULES
################
# This section imports necessary modules.
import os
import pandas as pd
import numpy as np
import plotly
from plotly.graph_objs import Box, Layout

#############
# IMPORT DATA
#############
# This section imports data.

# Set working directory.
# This obviously needs to be changed depending on the computer being used.
os.chdir('D:\\Users\\JBansal\\Documents\\GitHub\\visualizations')

# Load data.
census_data = pd.read_csv('census_data.csv',
                          encoding = 'latin-1')

################
# TRANSFORM DATA
################
# This section prepares the data for plotting.

# Remove row for aggregated United States.
census_data = census_data[census_data.Name != 'United States']

###########
# PLOT DATA
###########
# This section plots the data.

# Add boxplot data.
sixty = Box(y = round(census_data['1960'], 2),
            name = '1960')
seventy = Box(y = round(census_data['1970'], 2),
              name = '1970')
eighty = Box(y = round(census_data['1980'], 2),
             name = '1980')
ninety = Box(y = round(census_data['1990'], 2),
             name = '1990')
hundred = Box(y = round(census_data['2000'], 2),
              name = '2000')
ten = Box(y = round(census_data['2010'], 2),
          name = '2010')

# Add layout.
layout = Layout(title = 'Boxplots of US State Populations by Year',
                xaxis = dict(title = 'Year'),
                yaxis = dict(title = 'Population (tens of millions)'),
                font = dict(size = 20))

# Plot data.
boxplot_data = [sixty, seventy, eighty, ninety, hundred, ten]
plotly.offline.plot(dict(data = boxplot_data,
                         layout = layout))
