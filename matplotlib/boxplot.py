# This script creates a boxplot using 'census_data.csv'.

################
# IMPORT MODULES
################
# This section imports necessary modules.
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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

# Collect data in list for plotting.
boxplot_data = [census_data['1960'], census_data['1970'], census_data['1980'],
                census_data['1990'], census_data['2000'], census_data['2010']]

###########
# PLOT DATA
###########
# This section plots the data.

# Create figure and subplot.
fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)

# Add boxplot data.
plt.boxplot(boxplot_data)

# Add title and axis title.
plt.title('Boxplots of US State Populations by Year')
plt.xlabel('Year')
plt.ylabel('Population (tens of millions)')

# Set x-axis labels.
plt.xticks([1, 2, 3, 4, 5, 6],
           ['1960', '1970', '1980', '1990', '2000', '2010'])

# Plot data.
plt.show()
