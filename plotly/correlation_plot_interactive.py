# This script creates an interactive correlation plot using 'census_data.csv'.
# This chart type seems to be called a heatmap in most Python references.
# A description of 'census_data.csv' can be found in 'census_data_scrape_and_process.R'.

################
# IMPORT MODULES
################
# This section imports relevant modules for the script.
import os
import pandas as pd
import plotly
from plotly.graph_objs import Heatmap, Layout

#############
# IMPORT DATA
#############
# This section imports the data that will be used in the correlation plot.

# Set working directory.
# This obviously needs to be changed depending on the computer being used.
os.chdir('D:\\Users\\JBansal\\Documents\\GitHub\\visualizations')

# Import data.
census_data = pd.read_csv('census_data.csv',
                          encoding = 'latin-1')

############
# CLEAN DATA
############
# This section cleans the data so the correlation plot shows up properly.

# Remove 'Name' from 'census_data'.
# All correlation plot data must be numeric.
del(census_data['Name'])

# Remove null values from 'Area (sq. miles)'.
census_data = census_data.dropna()

# Rename 'Area (sq. miles)'.
# It's too long for the correlation plot.
census_data

##############
# ADD FEATURES
##############
# This section adds features to 'correlation_plot_data' that are negatively correlated with each other.
# This results in the correlation plot showing an example of how negative correlations look.

# Add population growth in percentage terms between 1960 and 1970.
census_data['60_70_growth'] = (census_data['1970'] - census_data['1960']) / census_data['1960']

# Add population growth in percentage terms between 1970 and 1980.
census_data['70_80_growth'] = (census_data['1980'] - census_data['1970']) / census_data['1970']

# Get 'census_data' correlations.
correlations  = round(census_data.corr(), 2)

#########################
# CREATE CORRELATION PLOT
#########################
# Plot correlation plot / heatmap.

# Create correlation plot data.
# I have to add 'y' before the year labels.
# Otherwise, plotly treats those as dates...
heatmap = Heatmap(z = correlations.values.tolist(),
                  x = ['y1960', 'y1970', 'y1980', 'y1990', 'y2000', 'y2010',
                       'Area', '60/70 Growth', '70/80 Growth'],
                  y = ['y1960', 'y1970', 'y1980', 'y1990', 'y2000', 'y2010',
                       'Area', '60/70 Growth', '70/80 Growth'])
heatmap_data = [heatmap]

# Add layout.
layout = Layout(title = 'Boxplots of US State Populations by Year',
                font = dict(size = 10))

# Plot data.
plotly.offline.plot(dict(data = heatmap_data,
                         layout = layout))
