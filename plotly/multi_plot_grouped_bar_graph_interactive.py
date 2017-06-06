# This script creates an interactive figure consisting of two subplots using 'census_data.csv'.

# A description of 'census_data.csv' can be found in 'census_data_scrape_and_process.R'.

# Calculations used below:
# Population percentage growth in a decade 't' will be computed as:
# 100 * (population(t + 1) - population(t)) / population(t)

# For example, the population growth between 1960 and 1970 is:
# 100 * (population(1970) - population(1960)) / population(1960)

################
# IMPORT MODULES
################
# This section imports necessary modules.
import os
import pandas as pd
import plotly
import plotly.graph_objs as pgo

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

# Compute percentage growth during 1960s decade (between 1960 and 1970):
census_data['1960s_growth'] = 100 * (census_data['1970'] - census_data['1960']) / census_data['1960']
  
# Compute percentage growth during 1970s decade (between 1970 and 1980):
census_data['1970s_growth'] = 100 * (census_data['1980'] - census_data['1970']) / census_data['1970']

# Compute percentage growth during 1980s decade (between 1980 and 1990):
census_data['1980s_growth'] = 100 * (census_data['1990'] - census_data['1980']) / census_data['1980']

# Compute percentage growth during 1990s decade (between 1990 and 2000):
census_data['1990s_growth'] = 100 * (census_data['2000'] - census_data['1990']) / census_data['1990']

# Compute percentage growth during 2000s decade (between 2000 and 2010):
census_data['2000s_growth'] = 100 * (census_data['2010'] - census_data['2000']) / census_data['2000']

# Specify rows of interest (states specified above and aggregate 'United States').
interest = ['Vermont', 'Delaware', 'Ohio', 'United States']

# Subset data.
census_subset = census_data[census_data['Name'].isin(interest)]

# Remove unneeded columns (all actual population measurements).
census_subset = census_subset[['Name', '1960s_growth', '1970s_growth', '1980s_growth', '1990s_growth', '2000s_growth']]

# Rename columns.
census_subset.columns = ['Name', '1960s', '1970s', '1980s', '1990s', '2000s']

# Melt data to allow plotting.
census_subset = pd.melt(census_subset,
                        id_vars = 'Name')

###########
# PLOT DATA
###########
# This section plots the data.

# Add data.
vt = pgo.Bar(x = census_subset[census_subset.Name == 'Vermont'].variable,
             y = round(census_subset[census_subset.Name == 'Vermont'].value, 2),
             name = 'Vermont')
de = pgo.Bar(x = census_subset[census_subset.Name == 'Delaware'].variable,
             y = round(census_subset[census_subset.Name == 'Delaware'].value, 2),
             name = 'Delaware')
oh = pgo.Bar(x = census_subset[census_subset.Name == 'Ohio'].variable,
             y = round(census_subset[census_subset.Name == 'Ohio'].value, 2),
             name = 'Ohio')
us = pgo.Bar(x = census_subset[census_subset.Name == 'United States'].variable,
             y = round(census_subset[census_subset.Name == 'United States'].value, 2),
             name = 'United States')

# Generate subplot structure.
figure = plotly.tools.make_subplots(rows = 2,
                                    cols = 1)

# Add data to appropriate subplot.
figure.append_trace(vt, 1, 1)
figure.append_trace(de, 1, 1)
figure.append_trace(oh, 1, 1)
figure.append_trace(us, 2, 1)

# Add layout.
figure['layout'].update(title = 'Percentage Growth by Decade For Selected States and Overall US')
figure['layout']['yaxis1'].update(title = 'Percentage Growth',
                                  range = [0, 25])
figure['layout']['yaxis2'].update(title = 'Percentage Growth',
                                  range = [0, 25])

# Plot data.
plotly.offline.plot(figure)






