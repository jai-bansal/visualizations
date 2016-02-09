# This script creates a stacked column chart using (a subset of) 'census_data.csv'.

# A description of 'census_data.csv' can be found in 'census_data_scrape_and_process.R'.
# To avoid an overwhelming plot, I will be using a subset of 'census_data.csv' consisting of
# all observations for the 'Southwest' region.

# This region is defined by the Bureau of Economic Analysis and can be viewed at the url below:
# https://en.wikipedia.org/wiki/List_of_regions_of_the_United_States

# The 'Southwest' region consists of Arizona, New Mexico, Texas, and Oklahoma.

# Import modules.
import pandas as pd
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

# Define 'Southwest' region.
southwest = ['Arizona', 'New Mexico', 'Texas', 'Oklahoma']

# Subset data.
census_subset = census_data[census_data['Name'].isin(southwest)]

# Melt 'census_subset' to allow stacked bar graph and change column names.
census_subset = pd.melt(census_subset, id_vars = 'Name')
census_subset.columns = ['State', 'Year', 'Population']

# Create new data subset to help with plotting.
# This will contain y-coordinates for the stacked bars.
plot_help = census_subset

# Un-melt 'plot_help' so that each column contains the populations for one state.
plot_help = plot_help.pivot(index = 'Year', columns = 'State')

# Add 'Arizona' and 'New Mexico' populations.
plot_help['az_nm'] = plot_help['Population']['Arizona'] + plot_help['Population']['New Mexico']

# Add 'Arizona', 'New Mexico', and 'Oklahoma' populations.
plot_help['az_nm_ok'] = plot_help['Population']['Arizona'] + plot_help['Population']['New Mexico'] + plot_help['Population']['Oklahoma']

# PLOT DATA.

# Create figure and subplot.
fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)

# Plot bars for each state.
ax1.bar(range(0, 6), census_subset[census_subset['State'] == 'Arizona']['Population'], label = 'Arizona', color = 'red',
        align = 'center', zorder = 3)
ax1.bar(range(0, 6), census_subset[census_subset['State'] == 'New Mexico']['Population'], label = 'New Mexico', color = 'blue',
        bottom = plot_help['Population']['Arizona'], align = 'center', zorder = 3)
ax1.bar(range(0, 6), census_subset[census_subset['State'] == 'Oklahoma']['Population'], label = 'Oklahoma', color = 'yellow',
        bottom = plot_help['az_nm'], align = 'center', zorder = 3)
ax1.bar(range(0, 6), census_subset[census_subset['State'] == 'Texas']['Population'], label = 'Texas', color = 'green',
        bottom = plot_help['az_nm_ok'], align = 'center', zorder = 3)

# Fix x-axis labels.
plt.xticks(range(0, 6), [1960, 1970, 1980, 1990, 2000, 2010], horizontalalignment = 'center')

# Remove ticks from both axes.
ax1.tick_params(axis = 'both', length = 0)



# Set plot and axes titles.
plt.title('Southwestern Region Population (in thousands) by Year and State', fontweight = 'bold')
plt.xlabel('Year', fontweight = 'bold', fontsize = 12.5)
plt.ylabel('Population (in thousands)', fontweight = 'bold', fontsize = 12.5)

# Add grid.
ax1.grid(zorder = 0)

# Add legend.
plt.legend(loc = 'left')

# Show plot.
plt.show()
