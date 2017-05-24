# This script creates a pie chart using (a subset of) 'census_data.csv'.

# A description of 'census_data.csv' can be found in 'census_data_scrape_and_process.R'.
# To avoid an overwhelming plot, I will be using a subset of 'census_data.csv' consisting of
# observations for 6 states (North Carolina, Maryland, New Jersey, Pennsylvania, Virginia, 
# and New York) in 2010.

# Import modules.
import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

# Set style.
style.use('seaborn-talk')

# Set working directory.
# This obviously needs to be changed depending on the computer being used.
os.chdir('D:\\Users\\JBansal\\Documents\\GitHub\\visualizations')

# Load data.
census_data = pd.read_csv('census_data.csv',
                          encoding = 'latin-1')

# SUBSET/PROCESS DATA.

# Specify states of interest.
states = ['North Carolina', 'Maryland', 'New Jersey', 'Pennsylvania', 'Virginia', 'New York']

# Create data subset (specified above).
census_subset = census_data[census_data['Name'].isin(states)][['Name', '2010']]

# Divide '2010' population value by 1000000 for easier graph viewing.
census_subset['2010']= census_subset['2010'] / 1000000

# PLOT DATA.

# Create figure and subplot.
fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)

# Specify pie chart labels.
labels = census_subset['Name']

# Specify pie chart slice sizes.
sizes = census_subset['2010']

# Add pie chart data.
one, two, three = ax1.pie(sizes,
        labels = labels,
        autopct = '%1.1f%%')

# Set state label font size.
two[0].set_fontsize(19)
two[1].set_fontsize(19)
two[2].set_fontsize(19)
two[3].set_fontsize(19)
two[4].set_fontsize(19)
two[5].set_fontsize(19)

# Set percentage label font size.
three[0].set_fontsize(19)
three[1].set_fontsize(19)
three[2].set_fontsize(19)
three[3].set_fontsize(19)
three[4].set_fontsize(19)
three[5].set_fontsize(19)

# Remove weird default pie chart tilt.
plt.axis('equal')

# Adjust plot title spacing.
ax1.title.set_position([0.5, 0.9])

# Set plot titles.
plt.title('Selected States 2010 Population (millions) and Percentage',
          fontweight = 'bold',
          fontsize = 20)

# Adjust plot margins.
plt.subplots_adjust(left = 0.25,
                    bottom = 0.0,
                    right = 0.67,
                    top = 0.95)

# Add legend.
legend = plt.legend(title = 'Population\n(millions)',
           labels = census_subset['2010'].round(1),
           fontsize = 18,
           bbox_to_anchor = (1.75, 0.78))
plt.setp(legend.get_title(), fontsize = 19)

# Show plot.
plt.show()
