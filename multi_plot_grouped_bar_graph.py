# This script creates a figure consisting of two subplots using (a subset of) 'census_data.csv'.

# A description of 'census_data.csv' can be found in 'census_data_scrape_and_process.R'.
# To avoid an overwhelming plot, I will be using a subset of 'census_data.csv'.

# The first subplot will be a grouped bar graph that uses all observations for 3 states: Vermont, Delaware, and Ohio
# It will show the percentage growth between decades for each state.
# The second subplot will be a bar graph that uses the aggregate United States observations
# and shows the percentage growth between decades for the entire United States.

# Population percentage growth in a decade 't' will be computed as:
# 100 * (population(t + 1) - population(t)) / population(t)

# For example, the population growth between 1960 and 1970 is:
# 100 * (population(1970) - population(1960)) / population(1960)

# Import modules.
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

# Set style.
style.use('ggplot')

# Load data.
census_data = pd.read_csv('census_data.csv',
                          encoding = 'latin-1')

# SUBSET/PROCESS DATA.

# Compute percentage growth during 1960s decade (between 1960 and 1970):
census_data['1960s_growth'] = 100 * (census_data['1970'] - census_data['1960']) / census_data['1960']
  
# Compute percentage growth during 1970s decade (between 1970 and 1980):
census_data['1970s_growth'] = 100 * (census_data['1980'] - census_data['1970']) / census_data['1970']

# Compute percentage growth during 1980s decade (between 1980 and 1990):
census_data['1980s_growth'] = 100 * (census_data['1990'] - census_data['1980']) / census_data['1980']

# Compute percentage growth during 1990s decade (between 1990 and 2000):
census_data['1990s_growth'] = 100 * (census_data['2000'] - census_data['1990']) / census_data['1990']

# Compute percentage growth during 2000s decade (between 2000 and 2010):
census_data['2000s_growth'] = 100 * (census_data['2010'] - census_data['2000']) / census_data['2000']

# Specify rows of interest (states specified above and aggregate 'United States').
interest = ['Vermont', 'Delaware', 'Ohio', 'United States']

# Subset data.
census_subset = census_data[census_data['Name'].isin(interest)]

# Remove unneeded columns (all actual population measurements).
census_subset = census_subset[['Name', '1960s_growth', '1970s_growth', '1980s_growth', '1990s_growth', '2000s_growth']]

# Melt data to allow plotting.
census_subset = pd.melt(census_subset,
                        id_vars = 'Name')

# PLOT DATA.

# Create figure.
fig = plt.figure()

# Create first subplot.
ax1 = fig.add_subplot(2, 1, 1)

# Add bars for each state to first subplot.
ax1.bar(range(0, 5),
        census_subset[census_subset['Name'] == 'Delaware']['value'],
        width = 0.3,
        color = '#ff5050',
        edgecolor = 'black',
        label = 'Delaware')
ax1.bar([0.3, 1.3, 2.3, 3.3, 4.3],
        census_subset[census_subset['Name'] == 'Ohio']['value'],
        width = 0.3,
        color = '#009933',
        edgecolor = 'black',
        label = 'Ohio')
ax1.bar([0.6, 1.6, 2.6, 3.6, 4.6],
        census_subset[census_subset['Name'] == 'Vermont']['value'],
        width = 0.3,
        color = '#8076ef',
        edgecolor = 'black',
        label = 'Vermont')

# Fix x-axis labels for first subplot.
plt.xticks([0.45, 1.45, 2.45, 3.45, 4.45, 5.45],
           ['1960s', '1970s', '1980s', '1990s', '2000s'],
           horizontalalignment = 'center')

# Set x-axis and y-axis limits for first subplot.
plt.ylim([0, 25])

# Adjust first subplot title spacing.
ax1.title.set_position([0.5, 1.05])

# Set title, x-axis, and y-axis labels for first subplot.
plt.title('Percentage Growth By Decade For Selected States',
          fontweight = 'bold')
plt.ylabel('Percentage Growth',
           fontweight = 'bold',
           fontsize = 12.5,
           color = 'black')

# For first subplot x-axis and y-axis: remove ticks, change tick labels to black and pick size.
ax1.tick_params(axis = 'both',
                length = 0,
                colors = 'black',
                labelsize = 12)

# Show legend for first subplot.
plt.legend()

# Create second subplot.
ax2 = fig.add_subplot(2, 1, 2,
                      sharex = ax1)

# Add bar for United States to second subplot.
ax2.bar([0.3, 1.3, 2.3, 3.3, 4.3],
        census_subset[census_subset['Name'] == 'United States']['value'],
        width = 0.3,
        color = '#ffcc00',
        edgecolor = 'black',
        label = 'United States')

# For second subplot x-axis and y-axis: remove ticks, change tick labels to black and pick size.
ax2.tick_params(axis = 'both',
                length = 0, 
                colors = 'black',
                labelsize = 12)

# Fix x-axis labels for second subplot.
plt.xticks([0.45, 1.45, 2.45, 3.45, 4.45],
           ['1960s', '1970s', '1980s', '1990s', '2000s'],
           horizontalalignment = 'center')

# Set y-axis limits for first subplot.
plt.ylim([0, 25])

# Adjust second subplot title spacing.
ax1.title.set_position([0.5, 1.03])

# Set title, x-axis, and y-axis labels for first subplot.
plt.title('Percentage Growth By Decade For United States',
          fontweight = 'bold')
plt.xlabel('Decade',
           fontweight = 'bold',
           fontsize = 12.5,
           color = 'black')
plt.ylabel('Percentage Growth',
           fontweight = 'bold',
           fontsize = 12.5,
           color = 'black')

# Add legend.
plt.legend()

# Adjust plot margins.
plt.subplots_adjust(left = 0.09,
                    bottom = 0.09,
                    right = 0.99,
                    top = 0.91,
                    hspace = 0.38)

# Show plot.
plt.show()
