# This script creates a correlation plot using 'census_data.csv'.
# A description of 'census_data.csv' can be found in 'census_data_scrape_and_process.R'.

################
# IMPORT MODULES
################
# This section imports relevant modules for the script.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn

#############
# IMPORT DATA
#############
# This section imports the data that will be used in the correlation plot.

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

#########################
# CREATE CORRELATION PLOT
#########################
# This section creates a correlation plot (using only numeric columns).

# Create correlation matrix.
correlation_matrix = census_data.corr()

# Create correlation plot.
seaborn.heatmap(correlation_matrix,
                xticklabels = correlation_matrix.columns.values,
                yticklabels = correlation_matrix.columns.values)

# Edit labels for visibility.
plt.xticks(rotation = 90)
plt.yticks(rotation = 0)

# View correlation plot.
plt.show()
