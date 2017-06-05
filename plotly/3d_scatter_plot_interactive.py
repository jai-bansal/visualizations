# This script creates a 3 dimensional scatter plot using (a subset of) 'census_data.csv'.

# A description of 'census_data.csv' can be found in 'census_data_scrape_and_process.R'.
# To avoid an overwhelming plot, I will be using a subset of 'census_data.csv' consisting of
# observations for 4 states (Maryland, Pennsylvania, Virginia, and West Virginia) in 2010.

################
# IMPORT MODULES
################
# This section imports relevant modules for the script.import os
import os
import pandas as pd
import plotly
from plotly.graph_objs import Scatter3d, Layout

#############
# IMPORT DATA
#############
# This section imports the data that will be used in the correlation plot.

# Set working directory.
# This obviously needs to be changed depending on the computer being used.
os.chdir('D:\\Users\\JBansal\\Documents\\GitHub\\visualizations')

# Load data.
census_data = pd.read_csv('census_data.csv',
                          encoding = 'latin-1')

######################
# CLEAN/TRANSFORM DATA
######################
# This section cleans the data so the correlation plot shows up properly.

# Divide population values by 1000000 for easier graph viewing.
census_data['1960'] = census_data['1960'] / 1000000
census_data['1970'] = census_data['1970'] / 1000000
census_data['1980'] = census_data['1980'] / 1000000
census_data['1990'] = census_data['1990'] / 1000000
census_data['2000'] = census_data['2000'] / 1000000
census_data['2010'] = census_data['2010'] / 1000000

# Specify states of interest.
states = ['Maryland', 'Pennsylvania', 'Virginia', 'West Virginia']

# Keep areas in separate data frame and rename columns.
areas = census_data[['Name', 'Area (sq. miles)']]
areas.columns = ['State', 'Area (sq. miles)']

# Divide state areas by 1000 for easier graph viewing.
areas['Area (sq. miles)'] = areas['Area (sq. miles)'] / 1000

# Create data subset.
census_subset = census_data[census_data['Name'].isin(states)][['Name', '1960', '1970', '1980', '1990', '2000', '2010']]

# Melt 'census_subset' to allow 3 dimensional scatter plot and rename columns.
census_subset = pd.melt(census_subset,
                        id_vars = 'Name')
census_subset.columns = ['State', 'Year', 'Population']

# Add 'areas' to 'census_subset'.
census_subset = census_subset.merge(areas,
                                    how = 'left',
                                    on = 'State')

###########
# PLOT DATA
###########
# This section plots the data.

# Add 3D scatter plot data.
md = Scatter3d(x = round(census_subset[census_subset.State == 'Maryland'].Population, 2),
               y = census_subset[census_subset.State == 'Maryland'].Year,
               z = round(census_subset[census_subset.State == 'Maryland']['Area (sq. miles)'], 2),
               name = 'Maryland')

pa = Scatter3d(x = round(census_subset[census_subset.State == 'Pennsylvania'].Population, 2),
               y = census_subset[census_subset.State == 'Pennsylvania'].Year,
               z = round(census_subset[census_subset.State == 'Pennsylvania']['Area (sq. miles)'], 2),
               name = 'Pennsylvania')

va = Scatter3d(x = round(census_subset[census_subset.State == 'Virginia'].Population, 2),
               y = census_subset[census_subset.State == 'Virginia'].Year,
               z = round(census_subset[census_subset.State == 'Virginia']['Area (sq. miles)'], 2),
               name = 'Virginia')

wv = Scatter3d(x = round(census_subset[census_subset.State == 'West Virginia'].Population, 2),
               y = census_subset[census_subset.State == 'West Virginia'].Year,
               z = round(census_subset[census_subset.State == 'West Virginia']['Area (sq. miles)'], 2),
               name = 'West Virginia')

scatter_3d_data = [md, pa, va, wv]

# Add layout.
layout = Layout(title = 'Selected State Populations and Areas Over Time',
                scene = dict(xaxis = dict(title = 'Pop. (in millions)'),
                             yaxis = dict(title = 'Year'),
                             zaxis = dict(title = 'Area (thousand sq. miles)')))

# Plot data.
plotly.offline.plot(dict(data = scatter_3d_data,
                         layout = layout))















