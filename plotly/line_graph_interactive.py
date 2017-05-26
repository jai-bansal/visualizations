# This script creates an interactive line graph using 'census_data.csv'.

# A description of 'census_data.csv' can be found in 'census_data_scrape_and_process.R'.

################
# IMPORT MODULES
################

# Import modules.
import os
import pandas as pd
import numpy as np
import plotly
from plotly.graph_objs import Scatter, Layout

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

# Divide population values by 1000000 for easier graph viewing.
census_data['1960'] = census_data['1960'] / 1000000
census_data['1970'] = census_data['1970'] / 1000000
census_data['1980'] = census_data['1980'] / 1000000
census_data['1990'] = census_data['1990'] / 1000000
census_data['2000'] = census_data['2000'] / 1000000
census_data['2010'] = census_data['2010'] / 1000000

# Subset data.
census_subset = census_data[census_data['Name'].isin(['Pennsylvania', 'Illinois'])][['Name', '1960', '1970', '1980', '1990', '2000', '2010']]

# Reset 'census_subset' index.
census_subset.reset_index(drop = True,
                          inplace = True)

# Melt 'census_subset' to allow line graph and rename columns.
census_subset = pd.melt(census_subset,
                        id_vars = 'Name')
census_subset.columns = ['State', 'Year', 'Population']

###########
# PLOT DATA
###########

# Add Pennsylvania line.
penn = Scatter(x = census_subset['Year'].unique(),
               y = census_subset[census_subset['State'] == 'Pennsylvania']['Population'],
               name = 'Pennsylvania')

# Add Illinois line.
ill = Scatter(x = census_subset['Year'].unique(),
              y = census_subset[census_subset['State'] == 'Illinois']['Population'],
              name = 'Illinois')

# Add layout.
layout = dict(title = 'Population (in milions) Over Time for Selected States',
              xaxis = dict(title = 'Year'),
              yaxis = dict(title = 'Population (in millions)'))

# Plot.
line_graph = [penn, ill]
plotly.offline.plot(dict(data = line_graph,
                         layout = layout))
