# This script creates an interactive scatter plot using 'census_data.csv'.

# A description of 'census_data.csv' can be found in 'census_data_scrape_and_process.R'.

################
# IMPORT MODULES
################

# Import modules.
import os
import pandas as pd
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

# Specify states of interest.
states = ['North Carolina', 'Maryland', 'New Jersey', 'Pennsylvania', 'Virginia', 'New York']

# Create data subset (specified above).
census_subset = census_data[census_data['Name'].isin(states)][['Name', '1960', '1970', '1980', '1990', '2000', '2010']]

# Melt 'census_subset' to allow line graph and rename columns.
census_subset = pd.melt(census_subset,
                        id_vars = 'Name')
census_subset.columns = ['State', 'Year', 'Population']

###########
# PLOT DATA
###########

# Add state markers.
nc = Scatter(x = census_subset['Year'].unique(),
             y = round(census_subset[census_subset['State'] == 'North Carolina']['Population'], 2),
             name = 'North Carolina',
             mode = 'markers')
md = Scatter(x = census_subset['Year'].unique(),
             y = round(census_subset[census_subset['State'] == 'Maryland']['Population'], 2),
             name = 'Maryland',
             mode = 'markers')
nj = Scatter(x = census_subset['Year'].unique(),
             y = round(census_subset[census_subset['State'] == 'New Jersey']['Population'], 2),
             name = 'New Jersey',
             mode = 'markers')
pa = Scatter(x = census_subset['Year'].unique(),
             y = round(census_subset[census_subset['State'] == 'Pennsylvania']['Population'], 2),
             name = 'Pennsylvania',
             mode = 'markers')
va = Scatter(x = census_subset['Year'].unique(),
             y = round(census_subset[census_subset['State'] == 'Virginia']['Population'], 2),
             name = 'Virginia',
             mode = 'markers')
ny = Scatter(x = census_subset['Year'].unique(),
             y = round(census_subset[census_subset['State'] == 'New York']['Population'], 2),
             name = 'New York',
             mode = 'markers')

# Add layout.
layout = dict(title = 'Selected State Populations (in millions) Over Time',
              xaxis = dict(title = 'Year'),
              yaxis = dict(title = 'Population (in millions)'),
              font = dict(size = 18))

# Plot.
scatter_plot = [nc, md, nj, pa, va, ny]
plotly.offline.plot(dict(data = scatter_plot,
                         layout = layout))
