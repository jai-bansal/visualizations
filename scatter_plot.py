# This script creates a scatter plot using (a subset of) 'census_data.csv'.

# A description of 'census_data.csv' can be found in 'census_data_scrape_and_process.R'.
# To avoid an overwhelming plot, I will be using a subset of 'census_data.csv' consisting of
# all observations for 6 states (North Carolina, Maryland, New Jersey, Pennsylvania, Virginia, 
# and New York).

# Import modules.
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

# Set style.
style.use('ggplot')

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

# Specify states of interest.
states = ['North Carolina', 'Maryland', 'New Jersey', 'Pennsylvania', 'Virginia', 'New York']

# Create data subset (specified above).
census_subset = census_data[census_data['Name'].isin(states)]

# Melt 'census_subset' to allow line graph and rename columns.
census_subset = pd.melt(census_subset, id_vars = 'Name')
census_subset.columns = ['State', 'Year', 'Population']

# PLOT DATA.

# Create figure and subplot.
fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)

# Add scatter plot data.
plt.scatter(census_subset['Year'].unique().tolist(), census_subset[census_subset['State'] == 'North Carolina']['Population'],
            label = 'North Carolina', marker = 'o', color = '#ff5050')
plt.scatter(census_subset['Year'].unique().tolist(), census_subset[census_subset['State'] == 'Maryland']['Population'],
            label = 'Maryland', marker = 'v', color = '#ffcc00')
plt.scatter(census_subset['Year'].unique().tolist(), census_subset[census_subset['State'] == 'New Jersey']['Population'],
            label = 'New Jersey', marker = 's', color = '#009933')
plt.scatter(census_subset['Year'].unique().tolist(), census_subset[census_subset['State'] == 'Pennsylvania']['Population'],
            label = 'Pennsylvania', marker = '*', color = '#614126')
plt.scatter(census_subset['Year'].unique().tolist(), census_subset[census_subset['State'] == 'Virginia']['Population'],
            label = 'Virginia', marker = '+', color = '#000099')
plt.scatter(census_subset['Year'].unique().tolist(), census_subset[census_subset['State'] == 'New York']['Population'],
            label = 'New York', marker = 'x', color = '#cc00ff')

# Remove ticks from both axes.
ax1.tick_params(axis = 'both', length = 0)

# Set x-axis and y-axis label text to black.
ax1.tick_params(axis = 'both', colors = 'black')

# Set y-axis limits.
plt.ylim([0, 20000])

# Set plot and axes titles.
plt.title('Selected State Populations (in thousands) Over Time', fontweight = 'bold')
plt.xlabel('Year', fontweight = 'bold', fontsize = 12.5, color = 'black')
plt.ylabel('Population (in thousands)', fontweight = 'bold', fontsize = 12.5, color = 'black')

##best
##	center
##	right
##	upper right
##	lower center
##	center left
##	lower right
##	upper left
##	upper center
##	lower left
##	center right

# Add legend.
plt.legend(bbox_to_anchor = (1.35, 0.7))

# Show plot.
plt.show()
