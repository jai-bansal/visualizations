# This script creates a bar graph using (a subset of) 'census_data.csv'.

# A description of 'census_data.csv' can be found in 'census_data_scrape_and_process.R'.
# To avoid an overwhelming plot, I will be using a subset of 'census_data.csv' consisting of
# observations for 6 states (Delaware, Maryland, New Jersey, Pennsylvania, Virginia, 
# and West Virginia) in 2010.

# Import modules.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load data.
census_data = pd.read_csv('census_data.csv', encoding = 'latin-1')

# SUBSET/PROCESS DATA.

# Specify states of interest.
states = ['Delaware', 'Maryland', 'New Jersey', 'Pennsylvania', 'Virginia', 'West Virginia']

# Create data subset.
census_subset = census_data[census_data['Name'].isin(states)]
census_subset = census_subset[['Name', '2010']]

# Reset 'census_subset' index.
census_subset.reset_index(drop = True, inplace = True)

# Divide population values by 1000 for easier graph viewing.
census_subset['2010'] = census_subset['2010'] / 1000

# PLOT DATA.

# Create figure and subplot.
# This typically isn't necessary since there's only 1 subplot, but will help in annotating
# the bars.
fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)

# Set colors.
colors = ['#ff5050', '#ffcc00', '#009933', '#00ffcc', '#000099', '#cc00ff']

# Introduce 'shift' parameter.
# This parameter helps space out the bars so there's enough room for labels.
shift = 1.3

# Insert plot data.
# This must be done in an absurd way since 'matplotlib.pyplot' can't handle strings.
bars = ax1.bar(np.arange(0, (shift * len(census_subset['2010'])), shift), census_subset['2010'],
               align = 'center',
               color = colors,
               zorder = 3)

# Annotate bars with '2010' population values.
for i in range(0, len(census_subset['Name'])):
    plt.text((i * shift), (bars[i].get_height() + 350),
             round(bars[i].get_height(), 1),
             horizontalalignment = 'center',
             verticalalignment = 'center')

# Remove ticks from both axes.
ax1.tick_params(axis = 'both', length = 0)

# Fix x-axis labels.
plt.xticks(np.arange(0, (shift * len(census_subset['2010'])), shift),
           states,
           horizontalalignment = 'center')

# Set plot and axes titles.
plt.title('Selected State Populations in 2010 (in thousands)', fontweight = 'bold')
plt.xlabel('State', fontweight = 'bold', fontsize = 12.5)
plt.ylabel('2010 Population (in thousands)', fontweight = 'bold', fontsize = 12.5)

# Add grid.
ax1.grid(zorder = 0)

# Adjust plot margins.
plt.subplots_adjust(top = 0.94 , bottom = 0.09, left = 0.12, right = 0.98)

fig.patch.set_facecolor('lightgray')

# Show plot.      
plt.show()
