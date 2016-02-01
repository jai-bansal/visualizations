# This script creates a line graph using (a subset of) 'census_data.csv'.

# A description of 'census_data.csv' can be found in 'census_data_scrape_and_process.R'.
# To avoid an overwhelming plot, I will be using a subset of 'census_data.csv' consisting of
# all observations for Pennsylvania and Illinois.

# Import modules.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load data.
census_data = pd.read_csv('census_data.csv', encoding = 'latin-1')

# SUBSET/PROCESS DATA.

# Divide population values by 1000 for easier graph viewing.
census_data['1960'] = census_data['1960'] / 1000
census_data['1970'] = census_data['1970'] / 1000
census_data['1980'] = census_data['1980'] / 1000
census_data['1990'] = census_data['1990'] / 1000
census_data['2000'] = census_data['2000'] / 1000
census_data['2010'] = census_data['2010'] / 1000

# Subset data.
census_subset = census_data[census_data['Name'].isin(['Pennsylvania', 'Illinois'])]

# Reset 'census_subset' index.
census_subset.reset_index(drop = True, inplace = True)

# Melt 'census_subset' to allow line graph and rename columns.
census_subset = pd.melt(census_subset, id_vars = 'Name')
census_subset.columns = ['State', 'Year', 'Population']

# PLOT DATA.

# Create figure and subplot.
fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)

# Add data.
ax1.plot(census_subset['Year'].unique(), census_subset[census_subset['State'] == 'Pennsylvania']['Population'],
         color = 'b', label = 'Pennsylvania')
ax1.plot(census_subset['Year'].unique(), census_subset[census_subset['State'] == 'Illinois']['Population'],
         color = 'r', label = 'Illinois')

ax1.scatter(census_subset['Year'], census_subset['Population'])

# Add plot labels.
ax1.annotate(round(census_subset[(census_subset['State'] == 'Illinois') & (census_subset['Year'] == '1960')]['Population'].values[0], 2),
             xy = (1957, 9950), xytext = (1957, 9950))
ax1.annotate(round(census_subset[(census_subset['State'] == 'Pennsylvania') & (census_subset['Year'] == '1960')]['Population'].values[0], 2),
             xy = (1957, 11200), xytext = (1957, 11200))
ax1.annotate(round(census_subset[(census_subset['State'] == 'Illinois') & (census_subset['Year'] == '2010')]['Population'].values[0], 2),
             xy = (2006, 12875), xytext = (2006, 12875))
ax1.annotate(round(census_subset[(census_subset['State'] == 'Pennsylvania') & (census_subset['Year'] == '2010')]['Population'].values[0], 2),
             xy = (2007, 12500), xytext = (2007, 12500))

# Set x-axis and y-axis limits.
plt.ylim([9900, 13100])
plt.xlim([1955, 2015])

# Remove first and last x-axis label (not needed).
ax1.xaxis.get_major_ticks()[0].label1.set_visible(False)
ax1.xaxis.get_major_ticks()[-1].label1.set_visible(False)

# Remove ticks from both axes.
ax1.tick_params(axis = 'both', length = 0)

# Set plot and axes titles.
plt.title('Population (in thousands) Over Time for 2 States', fontweight = 'bold')
plt.xlabel('Year', fontweight = 'bold', fontsize = 12.5)
plt.ylabel('Population (in thousands)', fontweight = 'bold', fontsize = 12.5)

# Add grid.
ax1.grid(zorder = 0)

# Add legend.
ax1.legend(loc = 2)

# Show plot.
plt.show()
