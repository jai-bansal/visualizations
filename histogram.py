# This script creates a histogram using (a subset of) 'census_data.csv'.

# A description of 'census_data.csv' can be found in 'census_data_scrape_and_process.R'.
# To avoid an overwhelming plot, I will be using a subset of 'census_data.csv' consisting of
# all observations for 2010.

# Import modules.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

# Set style.
style.use('dark_background')

# Load data.
census_data = pd.read_csv('census_data.csv', encoding = 'latin-1')

# SUBSET/PROCESS DATA.

# Create data subset consisting of all 2010 observations.
census_subset = census_data[['Name', '2010']]

# Remove row containing total population of United States.
census_subset = census_subset[census_subset['Name'] != 'United States']

# Divide population values by 1000 for easier graph viewing.
census_subset['2010'] = census_subset['2010'] / 1000

# PLOT DATA.

# Create figure and subplot.
fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)

# Add data.
ax1.hist(census_subset['2010'], bins = 19, color = 'darkgreen')

# Add annotations for Texas and California.
ax1.annotate('Texas', xy = ((census_subset[census_subset['Name'] == 'Texas']['2010']), 1),
             xytext = ((census_subset[census_subset['Name'] == 'Texas']['2010'] - 4000), 3.75), fontsize = 13)
ax1.annotate('(' + str(round(census_subset[census_subset['Name'] == 'Texas']['2010'].values[0], 1)) + ')',
             xy = ((census_subset[census_subset['Name'] == 'Texas']['2010'] - 400), 1),
             xytext = ((census_subset[census_subset['Name'] == 'Texas']['2010'] - 4000), 3), fontsize = 13,
             arrowprops = dict(arrowstyle = '->'))
ax1.annotate('California', xy = ((census_subset[census_subset['Name'] == 'California']['2010']), 1),
             xytext = ((census_subset[census_subset['Name'] == 'California']['2010']- 5000), 3.75), fontsize = 13)
ax1.annotate('(' + str(round(census_subset[census_subset['Name'] == 'California']['2010'].values[0], 1)) + ')',
             xy = ((census_subset[census_subset['Name'] == 'California']['2010'] - 900), 1),
             xytext = ((census_subset[census_subset['Name'] == 'California']['2010'] - 5000), 3), fontsize = 13,
             arrowprops = dict(arrowstyle = '->'))

# Remove ticks from both axes.
ax1.tick_params(axis = 'both', length = 0)

# Set plot and axes titles.
plt.title('Frequency of 2010 US State Populations (in thousands)', fontweight = 'bold')
plt.xlabel('2010 Populations (in thousands)', fontweight = 'bold', fontsize = 12.5, color = 'white')
plt.ylabel('Frequency', fontweight = 'bold', fontsize = 12.5, color = 'white')

# Adjust plot margins.
plt.subplots_adjust(left = 0.08, bottom = 0.09, right = 0.95, top = 0.93)

# Show plot.
plt.show()
