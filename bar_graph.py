# This script creates a bar graph using (a subset of) 'census_data.csv'.

# A description of 'census_data.csv' can be found in 'census_data_scrape_and_process.R'.
# To avoid an overwhelming plot, I will be using a subset of 'census_data.csv' consisting of
# observations for 6 states (Delaware, Maryland, New Jersey, Pennsylvania, Virginia, 
# and West Virginia) in 2010.

# Import modules.
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.style

# Set style.
#matplotlib.style.use('ggplot')

# Load data.
census_data = pd.read_csv('census_data.csv', encoding = 'latin-1')

# SUBSET/PROCESS DATA.

# Specify states of interest.
states = ['Delaware', 'Maryland', 'New Jersey', 'Pennsylvania', 'Virginia', 'West Virginia']

# Create data subset.
census_subset = census_data[census_data['Name'].isin(states)]
census_subset = census_subset[['Name', '2010']]

# Divide population values by 1000 for easier graph viewing.
census_subset['2010'] = census_subset['2010'] / 1000

# PLOT DATA.

# Set colors.
colors = ['#ff5050', '#ffcc00', '#009933', '#00ffcc', '#000099', '#cc00ff']

# Insert plot data.
# This must be done in an absurd way since 'matplotlib.pyplot' can't handle strings.
plt.bar(range(0, len(census_subset['Name'])), census_subset['2010'], align = 'center',
        color = colors, zorder = 3)

# Fix x-axis labels.
plt.xticks(range(0, len(census_subset['Name'])), states, fontsize = 10)

# Remove ticks from both axes.
plt.tick_params(axis = 'both', length = 0)

# Set plot and axes titles.
plt.title('Selected State Populations in 2010 (in thousands)', fontweight = 'bold')
plt.xlabel('State', fontweight = 'bold')
plt.ylabel('2010 Population (in thousands)', fontweight = 'bold')

# Add labels for each bar.
for i in range(0, 6):
    plt.annotate(census_subset['Name'][i], xy
    print(i)

# Add grid.
plt.grid(zorder = 0)

# Adjust plot margins.
plt.subplots_adjust(top = 0.94 , bottom = 0.09, left = 0.12, right = 0.98)

# Show plot.
plt.show()
