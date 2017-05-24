# This script creates a bar graph using (a subset of) 'census_data.csv'.

# A description of 'census_data.csv' can be found in 'census_data_scrape_and_process.R'.
# To avoid an overwhelming plot, I will be using a subset of 'census_data.csv' consisting of
# observations for 6 states (Delaware, Maryland, New Jersey, Pennsylvania, Virginia, 
# and West Virginia) in 2010.

# Import modules.
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Set working directory.
# This obviously needs to be changed depending on the computer being used.
os.chdir('D:\\Users\\JBansal\\Documents\\GitHub\\visualizations')

# Load data.
census_data = pd.read_csv('census_data.csv',
                          encoding = 'latin-1')

# SUBSET/PROCESS DATA.

# Specify states of interest.
states = ['Delaware', 'Maryland', 'New Jersey', 'Pennsylvania', 'Virginia', 'West Virginia']

# Create data subset.
census_subset = census_data[census_data['Name'].isin(states)]
census_subset = census_subset[['Name', '2010']]

# Reset 'census_subset' index.
census_subset.reset_index(drop = True,
                          inplace = True)

# Divide population values by 1000000 for easier graph viewing.
census_subset['2010'] = census_subset['2010'] / 1000000

# PLOT DATA.

# Create figure and subplot.
fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)

# Set colors.
colors = ['#ff5050', '#ffcc00', '#009933', '#00ffcc', '#000099', '#cc00ff']

# Introduce 'shift' parameter.
# This parameter helps space out the bars so there's enough room for labels.
shift = 1.5

# Insert plot data.
# This must be done in an absurd way since 'matplotlib.pyplot' can't handle strings.
bars = ax1.bar(np.arange(0,
                         (shift * len(census_subset['2010'])),
                         shift),
               census_subset['2010'],
               align = 'center',
               color = colors,
               zorder = 3)

# Annotate bars with '2010' population values.
for i in range(0, len(census_subset['Name'])):
    plt.text((i * shift),
             (bars[i].get_height() + 0.35),
             round(bars[i].get_height(), 2),
             horizontalalignment = 'center',
             verticalalignment = 'center',
             fontsize = 14)

# Remove ticks from both axes.
ax1.tick_params(axis = 'both',
                length = 0)

# Adjust plot title spacing.
ax1.title.set_position([0.5, 1.035])

# Adjust x-axis and y-axis tick label size.
plt.tick_params(axis = 'both', labelsize = 12)

# Adjust x-axis.
plt.xlim([-0.75, 8.25])

# Adjust x-axis title spacing.
ax1.xaxis.labelpad = 10

# Fix x-axis labels.
plt.xticks(np.arange(0,
                     (shift * len(census_subset['2010'])),
                     shift),
           states,
           horizontalalignment = 'center')

# Set plot and axes titles.
plt.title('Selected State Populations in 2010 (in millions)',
          fontweight = 'bold',
          fontsize = 16)
plt.xlabel('State',
           fontweight = 'bold',
           fontsize = 14)
plt.ylabel('2010 Population (in millions)',
           fontweight = 'bold',
           fontsize = 14)

# Add grid.
ax1.grid(zorder = 0)

# Adjust plot margins.
plt.subplots_adjust(left = 0.12,
                    bottom = 0.11,
                    right = 0.98,
                    top = 0.9)

# Show plot.      
plt.show()
