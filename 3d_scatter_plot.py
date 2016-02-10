# This script creates a 3 dimensional scatter plot using (a subset of) 'census_data.csv'.

# A description of 'census_data.csv' can be found in 'census_data_scrape_and_process.R'.
# To avoid an overwhelming plot, I will be using a subset of 'census_data.csv' consisting of
# observations for 4 states (Maryland, Pennsylvania, Virginia, and West Virginia) in 2010.

# Import modules.
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from matplotlib import style

# Set style.
style.use('seaborn-pastel')

# Load data.
census_data = pd.read_csv('census_data.csv',
                          encoding = 'latin-1')

# SUBSET/PROCESS DATA.

# Divide population values by 1000 for easier graph viewing.
census_data['1960'] = census_data['1960'] / 1000
census_data['1970'] = census_data['1970'] / 1000
census_data['1980'] = census_data['1980'] / 1000
census_data['1990'] = census_data['1990'] / 1000
census_data['2000'] = census_data['2000'] / 1000
census_data['2010'] = census_data['2010'] / 1000

# Specify states of interest.
states = ['Maryland', 'Pennsylvania', 'Virginia', 'West Virginia']

# Keep areas in separate data frame and rename columns
areas = census_data[['Name', 'Area (sq. miles)']]
areas.columns = ['State', 'Area (sq. miles)']

# Create data subset.
census_subset = census_data[census_data['Name'].isin(states)][['Name', '1960', '1970', '1980', '1990', '2000', '2010']]

# Melt 'census_subset' to allow 3 dimensional scatter plot and rename columns.
census_subset = pd.melt(census_subset,
                        id_vars = 'Name')
census_subset.columns = ['State', 'Year', 'Population']

# Add 'areas' to 'census_subset'.
census_subset = census_subset.merge(areas,
                                    how = 'left',
                                    on = 'State')

# PLOT DATA.

# Create figure and subplot.
fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1,
                      projection = '3d')

# Add scatter plot points.
ax1.scatter([1,2,3,4,5,6],
            census_subset[census_subset['State'] == 'Maryland']['Population'],
            census_subset[census_subset['State'] == 'Maryland']['Area (sq. miles)'],
            label = 'Maryland',
            c = '#ffcc00')
ax1.scatter([1,2,3,4,5,6],
            census_subset[census_subset['State'] == 'Pennsylvania']['Population'],
            census_subset[census_subset['State'] == 'Pennsylvania']['Area (sq. miles)'],
            label = 'Pennsylvania',
            c = '#614126')
ax1.scatter([1,2,3,4,5,6],
            census_subset[census_subset['State'] == 'Virginia']['Population'],
            census_subset[census_subset['State'] == 'Virginia']['Area (sq. miles)'],
            label = 'Virginia',
            c = '#000099')
ax1.scatter([1,2,3,4,5,6],
            census_subset[census_subset['State'] == 'West Virginia']['Population'],
            census_subset[census_subset['State'] == 'West Virginia']['Area (sq. miles)'],
            label = 'West Virginia',
            c = '#009933')

# Fix x-axis labels.
ax1.set_xticklabels([1960, 1970, 1980, 1990, 2000, 2010])

# Remove unneeded tick labels.
ax1.yaxis.get_major_ticks()[0].label1.set_visible(False)
ax1.yaxis.get_major_ticks()[-1].label1.set_visible(False)
ax1.zaxis.get_major_ticks()[0].label1.set_visible(False)
ax1.zaxis.get_major_ticks()[-1].label1.set_visible(False)

# Set plot and axes titles.
plt.title('Selected State Populations and Areas Over Time')
plt.xlabel('Year',
           fontsize = 12.5,
           color = 'black')
plt.ylabel('Population (in thousands)',
           fontsize = 12.5,
           color = 'black')
ax1.set_zlabel('Area (square miles)',
               fontsize = 12.5,
               color = 'black')

# Add legend.
plt.legend(scatterpoints = 1,
           bbox_to_anchor = (1.45, 0.6))

# Adjust plot margins.
plt.subplots_adjust(left = 0.12, bottom = 0.08, right = 0.73, top = 0.97)

# Show plot.
plt.show()
