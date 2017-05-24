# This script creates a histogram using (a subset of) 'census_data.csv'.

# A description of 'census_data.csv' can be found in 'census_data_scrape_and_process.R'.
# To avoid an overwhelming plot, I will be using a subset of 'census_data.csv' consisting of
# all observations for 2010.

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

# Create data subset consisting of all 2010 observations.
census_subset = census_data[['Name', '2010']]

# Remove row containing total population of United States.
census_subset = census_subset[census_subset['Name'] != 'United States']

# Divide population values by 1000000 for easier graph viewing.
census_subset['2010'] = census_subset['2010'] / 1000000

# PLOT DATA.

# Create figure and subplot.
fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)

# Add data.
ax1.hist(census_subset['2010'],
         bins = 20,
         color = 'darkgreen',
         zorder = 3,
         edgecolor = 'black',
         linewidth = 1)

# Add annotations for Texas and California.
ax1.annotate('Texas',
             xy = ((census_subset[census_subset['Name'] == 'Texas']['2010']), 1),
             xytext = ((census_subset[census_subset['Name'] == 'Texas']['2010'] - 4), 3.75),
             fontsize = 13,
             zorder = 3)
ax1.annotate('(' + str(round(census_subset[census_subset['Name'] == 'Texas']['2010'].values[0], 2)) + ')',
             xy = ((census_subset[census_subset['Name'] == 'Texas']['2010'] - 0.4), 1),
             xytext = ((census_subset[census_subset['Name'] == 'Texas']['2010'] - 4), 3),
             fontsize = 13,
             zorder = 3,
             arrowprops = dict(arrowstyle = '->'))
ax1.annotate('California',
             xy = ((census_subset[census_subset['Name'] == 'California']['2010']), 1),
             xytext = ((census_subset[census_subset['Name'] == 'California']['2010'] - 5), 3.75),
             zorder = 3,
             fontsize = 13)
ax1.annotate('(' + str(round(census_subset[census_subset['Name'] == 'California']['2010'].values[0], 2)) + ')',
             xy = ((census_subset[census_subset['Name'] == 'California']['2010'] - 0.9), 1),
             xytext = ((census_subset[census_subset['Name'] == 'California']['2010'] - 5), 3),
             fontsize = 13,
             zorder = 3,
             arrowprops = dict(facecolor = 'black',
                               arrowstyle = '->'))

# For x-axis and y-axis: remove ticks, change tick labels to black and pick size.
ax1.tick_params(axis = 'both',
                length = 0,
                colors = 'black',
                labelsize = 14)

# Remove last x-axis label (not needed).
ax1.xaxis.get_major_ticks()[-1].label1.set_visible(False)

# Adjust plot title spacing.
ax1.title.set_position([0.5, 1.02])

# Adjust x-axis title spacing.
ax1.xaxis.labelpad = 12

# Add grid.
ax1.grid(zorder = 0)

# Set plot and axes titles.
plt.title('Frequency of 2010 US State Populations (in millions)',
          fontweight = 'bold')
plt.xlabel('2010 Populations (in millions)',
           fontweight = 'bold',
           fontsize = 14,
           color = 'black')
plt.ylabel('Frequency',
           fontweight = 'bold',
           fontsize = 14,
           color = 'black')

# Adjust plot margins.
plt.subplots_adjust(left = 0.08,
                    bottom = 0.11,
                    right = 0.95,
                    top = 0.91)

# Show plot.
plt.show()
