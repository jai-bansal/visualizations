# This script creates an interactive violin plot using 'census_data.csv'.

################
# IMPORT MODULES
################
# This section imports necessary modules.
import os
import pandas as pd
import numpy as np
import plotly
import plotly.figure_factory as ff

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

# Divide population values by 1 million to get better violin plot look.
census_data['1960'] = census_data['1960'] / 1000000
census_data['1970'] = census_data['1970'] / 1000000
census_data['1980'] = census_data['1980'] / 1000000
census_data['1990'] = census_data['1990'] / 1000000
census_data['2000'] = census_data['2000'] / 1000000
census_data['2010'] = census_data['2010'] / 1000000

# Melt data in prepartion for plotting.
melted_data = pd.melt(census_data[['1960', '1970', '1980', '1990', '2000', '2010']],
                      value_vars = ['1960', '1970', '1980', '1990', '2000', '2010'])

###########
# PLOT DATA
###########
# This section plots the data.
violin_plot = ff.create_violin(melted_data,
                               data_header = 'value',
                               group_header = 'variable')
plotly.offline.plot(violin_plot)





