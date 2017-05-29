# This script creates an interactive pie chart using 'census_data.csv'.

# A description of 'census_data.csv' can be found in 'census_data_scrape_and_process.R'.

################
# IMPORT MODULES
################

# Import modules.
import os
import pandas as pd
import plotly
from plotly.graph_objs import Pie, Layout

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
states = ['North Carolina', 'Maryland', 'New Jersey', 'Pennsylvania', 'Virginia', 'New York']

# Create data subset (specified above).
census_subset = census_data[census_data['Name'].isin(states)][['Name', '2010']]

# Divide '2010' population value by 1000000 for easier graph viewing.
census_subset['2010']= census_subset['2010'] / 1000000

###########
# PLOT DATA
###########

# Specify pie chart data.
pie = Pie(labels = census_subset.Name,
          values = round(census_subset['2010'], 2))

# Add layout.
layout = Layout(dict(title = 'Selected States 2010 Population (millions) and Percentage',
                     font = dict(size = 24)))

# Plot pie chart.
pie_data = [pie]
plotly.offline.plot(dict(data = pie_data,
                         layout = layout))
