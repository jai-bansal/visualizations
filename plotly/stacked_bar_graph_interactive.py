# This script creates an interactive stacked column chart using 'census_data.csv'.

# A description of 'census_data.csv' can be found in 'census_data_scrape_and_process.R'.

# The 'Great Lakes' region as defined by the Bureau of Economic Analysis contains Wisconsin, Michigan, Illinois, Indiana, and Ohio.

################
# IMPORT MODULES
################

# Import modules.
import os
import pandas as pd
import plotly
from plotly.graph_objs import Bar, Layout

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

# Define 'Great Lakes' region.
great_lakes = ['Wisconsin', 'Michigan', 'Illinois', 'Indiana', 'Ohio']

# Subset data.
census_subset = census_data[census_data['Name'].isin(great_lakes)][['Name', '1960', '1970', '1980', '1990', '2000', '2010']]

# Melt 'census_subset' to allow stacked bar graph and change column names.
census_subset = pd.melt(census_subset,
                        id_vars = 'Name')
census_subset.columns = ['State', 'Year', 'Population']

# Create new data subset 'plot_help' to help with plotting.
# This will contain y-coordinates for the stacked bars.
plot_help = census_subset

# Un-melt 'plot_help' so that each column contains the populations for one state.
plot_help = plot_help.pivot(index = 'Year',
                            columns = 'State')

# Add 'Wisconsin' and 'Michigan' populations.
plot_help['wi_mi'] = plot_help['Population']['Wisconsin'] + plot_help['Population']['Michigan']

# Add 'Wisconsin', 'Michigan', and 'Illinois' populations.
plot_help['wi_mi_il'] = plot_help['Population']['Wisconsin'] + plot_help['Population']['Michigan'] + plot_help['Population']['Illinois']

# Add 'Wisconsin', 'Michigan', 'Illinois', and 'Indiana' populations.
plot_help['wi_mi_il_in'] = plot_help['Population']['Wisconsin'] + plot_help['Population']['Michigan'] + plot_help['Population']['Illinois'] + plot_help['Population']['Indiana']

# Add all state populations together.
plot_help['all'] = plot_help['Population']['Wisconsin'] + plot_help['Population']['Michigan'] + plot_help['Population']['Illinois'] + plot_help['Population']['Indiana'] + plot_help['Population']['Ohio']

###########
# PLOT DATA
###########

# Add state bars.
il = Bar(x = census_subset.Year.unique(),
         y = round(census_subset[census_subset['State'] == 'Illinois']['Population'], 2),
         name = 'Illinois')
ind = Bar(x = census_subset.Year.unique(),
          y = round(census_subset[census_subset['State'] == 'Indiana']['Population'], 2),
          name = 'Indiana')
mi = Bar(x = census_subset.Year.unique(),
         y = round(census_subset[census_subset['State'] == 'Michigan']['Population'], 2),
         name = 'Michigan')
oh = Bar(x = census_subset.Year.unique(),
         y = round(census_subset[census_subset['State'] == 'Ohio']['Population'], 2),
         name = 'Ohio')
wi = Bar(x = census_subset.Year.unique(),
         y = round(census_subset[census_subset['State'] == 'Wisconsin']['Population'], 2),
         name = 'Wisconsin')

# Add layout.
layout = Layout(dict(barmode = 'stack',
                     title = 'Great Lakes Region Population (in millions) by Year and State',
                     xaxis = dict(title = 'Year'),
                     yaxis = dict(title = 'Population (in millions)'),
                     font = dict(size = 20)))

# Plot data.
stacked_bar_graph_data = [il, ind, mi, oh, wi]
plotly.offline.plot(dict(data = stacked_bar_graph_data,
                         layout = layout))



