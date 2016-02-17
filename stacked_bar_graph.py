# This script creates a stacked column chart using (a subset of) 'census_data.csv'.

# A description of 'census_data.csv' can be found in 'census_data_scrape_and_process.R'.
# To avoid an overwhelming plot, I will be using a subset of 'census_data.csv' consisting of
# all observations for the 'Great Lakes' region.

# This region is defined by the Bureau of Economic Analysis and can be viewed at the url below:
# https://en.wikipedia.org/wiki/List_of_regions_of_the_United_States

# The 'Great Lakes' region as defined by the Bureau of Economic Analysis contains Wisconsin, Michigan, Illinois, Indiana, and Ohio.

# Import modules.
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

# Set style.
style.use('seaborn-poster')

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

# Define 'Great Lakes' region.
great_lakes = ['Wisconsin', 'Michigan', 'Illinois', 'Indiana', 'Ohio']

# Subset data.
census_subset = census_data[census_data['Name'].isin(great_lakes)][['Name', '1960', '1970', '1980', '1990', '2000', '2010']]

# Melt 'census_subset' to allow stacked bar graph and change column names.
census_subset = pd.melt(census_subset,
                        id_vars = 'Name')
census_subset.columns = ['State', 'Year', 'Population']

# Create new data subset 'plot_help' to help with plotting.
# This will contain y-coordinates for the stacked bars.
plot_help = census_subset

# Un-melt 'plot_help' so that each column contains the populations for one state.
plot_help = plot_help.pivot(index = 'Year',
                            columns = 'State')

# Add 'Wisconsin' and 'Michigan' populations.
plot_help['wi_mi'] = plot_help['Population']['Wisconsin'] + plot_help['Population']['Michigan']

# Add 'Wisconsin', 'Michigan', and 'Illinois' populations.
plot_help['wi_mi_il'] = plot_help['Population']['Wisconsin'] + plot_help['Population']['Michigan'] + plot_help['Population']['Illinois']

# Add 'Wisconsin', 'Michigan', 'Illinois', and 'Indiana' populations.
plot_help['wi_mi_il_in'] = plot_help['Population']['Wisconsin'] + plot_help['Population']['Michigan'] + plot_help['Population']['Illinois'] + plot_help['Population']['Indiana']

# Add all state populations together.
plot_help['all'] = plot_help['Population']['Wisconsin'] + plot_help['Population']['Michigan'] + plot_help['Population']['Illinois'] + plot_help['Population']['Indiana'] + plot_help['Population']['Ohio']

# PLOT DATA.

# Create figure and subplot.
fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)

# Plot bars for each state.
ax1.bar(range(0, 6),
        census_subset[census_subset['State'] == 'Wisconsin']['Population'],
        label = 'Wisconsin',
        color = '#ff5050',
        align = 'center',
        zorder = 3)
ax1.bar(range(0, 6),
        census_subset[census_subset['State'] == 'Michigan']['Population'],
        label = 'Michigan',
        color = '#ffcc00',
        bottom = plot_help['Population']['Wisconsin'],
        align = 'center',
        zorder = 3)
ax1.bar(range(0, 6),
        census_subset[census_subset['State'] == 'Illinois']['Population'],
        label = 'Illinois',
        color = '#009933',
        bottom = plot_help['wi_mi'],
        align = 'center',
        zorder = 3)
ax1.bar(range(0, 6),
        census_subset[census_subset['State'] == 'Indiana']['Population'],
        label = 'Indiana',
        color = '#e93fc7',
        bottom = plot_help['wi_mi_il'],
        align = 'center',
        zorder = 3)
ax1.bar(range(0, 6),
        census_subset[census_subset['State'] == 'Ohio']['Population'],
        label = 'Ohio',
        color = '#8076ef',
        bottom = plot_help['wi_mi_il_in'],
        align = 'center',
        zorder = 3)

# Fix x-axis labels.
plt.xticks(range(0, 6),
           [1960, 1970, 1980, 1990, 2000, 2010],
           horizontalalignment = 'center')

# Remove ticks from both axes.
ax1.tick_params(axis = 'both',
                length = 0)

# Remove last y-axis label (not needed).
ax1.yaxis.get_major_ticks()[-1].label1.set_visible(False)

# Add plot annotations.
# All annotations for a single state are done before starting a new state.
# This is messy and tedious. I don't think matplotlib pyplot is a good tool at all for this.

# Wisconsin.
ax1.annotate(round(plot_help['Population']['Wisconsin']['1960'], 1),
             xy = (0, (0.5 * plot_help['Population']['Wisconsin']['1960'])),
             xytext = (0, (0.5 * plot_help['Population']['Wisconsin']['1960'])),
             horizontalalignment = 'center',
             verticalalignment = 'center',
             fontsize = 16)
ax1.annotate(round(plot_help['Population']['Wisconsin']['1970'], 1),
             xy = (1, (0.5 * plot_help['Population']['Wisconsin']['1970'])),
             xytext = (1, (0.5 * plot_help['Population']['Wisconsin']['1970'])),
             horizontalalignment = 'center',
             verticalalignment = 'center',
             fontsize = 16)
ax1.annotate(round(plot_help['Population']['Wisconsin']['1980'], 1),
             xy = (2, (0.5 * plot_help['Population']['Wisconsin']['1980'])),
             xytext = (2, (0.5 * plot_help['Population']['Wisconsin']['1980'])),
             horizontalalignment = 'center',
             verticalalignment = 'center',
             fontsize = 16)
ax1.annotate(round(plot_help['Population']['Wisconsin']['1990'], 1),
             xy = (3, (0.5 * plot_help['Population']['Wisconsin']['1990'])),
             xytext = (3, (0.5 * plot_help['Population']['Wisconsin']['1990'])),
             horizontalalignment = 'center',
             verticalalignment = 'center',
             fontsize = 16)
ax1.annotate(round(plot_help['Population']['Wisconsin']['2000'], 1),
             xy = (4, (0.5 * plot_help['Population']['Wisconsin']['2000'])),
             xytext = (4, (0.5 * plot_help['Population']['Wisconsin']['2000'])),
             horizontalalignment = 'center',
             verticalalignment = 'center',
             fontsize = 16)
ax1.annotate(round(plot_help['Population']['Wisconsin']['2010'], 1),
             xy = (5, (0.5 * plot_help['Population']['Wisconsin']['2010'])),
             xytext = (5, (0.5 * plot_help['Population']['Wisconsin']['2010'])),
             horizontalalignment = 'center',
             verticalalignment = 'center',
             fontsize = 16)

# Michigan.
ax1.annotate(round(plot_help['Population']['Michigan']['1960'], 1),
             xy = (0, 0.5 * (plot_help['Population']['Wisconsin']['1960'] + plot_help['wi_mi']['1960'])),
             xytext = (0, 0.5 * (plot_help['Population']['Wisconsin']['1960'] + plot_help['wi_mi']['1960'])),
             horizontalalignment = 'center',
             verticalalignment = 'center',
             fontsize = 16)
ax1.annotate(round(plot_help['Population']['Michigan']['1970'], 1),
             xy = (1, 0.5 * (plot_help['Population']['Wisconsin']['1970'] + plot_help['wi_mi']['1970'])),
             xytext = (1, 0.5 * (plot_help['Population']['Wisconsin']['1970'] + plot_help['wi_mi']['1970'])),
             horizontalalignment = 'center',
             verticalalignment = 'center',
             fontsize = 16)
ax1.annotate(round(plot_help['Population']['Michigan']['1980'], 1),
             xy = (2, 0.5 * (plot_help['Population']['Wisconsin']['1980'] + plot_help['wi_mi']['1980'])),
             xytext = (2, 0.5 * (plot_help['Population']['Wisconsin']['1980'] + plot_help['wi_mi']['1980'])),
             horizontalalignment = 'center',
             verticalalignment = 'center',
             fontsize = 16)
ax1.annotate(round(plot_help['Population']['Michigan']['1990'], 1),
             xy = (3, 0.5 * (plot_help['Population']['Wisconsin']['1990'] + plot_help['wi_mi']['1990'])),
             xytext = (3, 0.5 * (plot_help['Population']['Wisconsin']['1990'] + plot_help['wi_mi']['1990'])),
             horizontalalignment = 'center',
             verticalalignment = 'center',
             fontsize = 16)
ax1.annotate(round(plot_help['Population']['Michigan']['2000'], 1),
             xy = (4, 0.5 * (plot_help['Population']['Wisconsin']['2000'] + plot_help['wi_mi']['2000'])),
             xytext = (4, 0.5 * (plot_help['Population']['Wisconsin']['2000'] + plot_help['wi_mi']['2000'])),
             horizontalalignment = 'center',
             verticalalignment = 'center',
             fontsize = 16)
ax1.annotate(round(plot_help['Population']['Michigan']['2010'], 1),
             xy = (5, 0.5 * (plot_help['Population']['Wisconsin']['2010'] + plot_help['wi_mi']['2010'])),
             xytext = (5, 0.5 * (plot_help['Population']['Wisconsin']['2010'] + plot_help['wi_mi']['2010'])),
             horizontalalignment = 'center',
             verticalalignment = 'center',
             fontsize = 16)

# Illinois.
ax1.annotate(round(plot_help['Population']['Illinois']['1960'], 1),
             xy = (0, 0.5 * (plot_help['wi_mi']['1960'] + plot_help['wi_mi_il']['1960'])),
             xytext = (0, 0.5 * (plot_help['wi_mi']['1960'] + plot_help['wi_mi_il']['1960'])),
             horizontalalignment = 'center',
             verticalalignment = 'center',
             fontsize = 16)
ax1.annotate(round(plot_help['Population']['Illinois']['1970'], 1),
             xy = (1, 0.5 * (plot_help['wi_mi']['1970'] + plot_help['wi_mi_il']['1970'])),
             xytext = (1, 0.5 * (plot_help['wi_mi']['1970'] + plot_help['wi_mi_il']['1970'])),
             horizontalalignment = 'center',
             verticalalignment = 'center',
             fontsize = 16)
ax1.annotate(round(plot_help['Population']['Illinois']['1980'], 1),
             xy = (2, 0.5 * (plot_help['wi_mi']['1980'] + plot_help['wi_mi_il']['1980'])),
             xytext = (2, 0.5 * (plot_help['wi_mi']['1980'] + plot_help['wi_mi_il']['1980'])),
             horizontalalignment = 'center',
             verticalalignment = 'center',
             fontsize = 16)
ax1.annotate(round(plot_help['Population']['Illinois']['1990'], 1),
             xy = (3, 0.5 * (plot_help['wi_mi']['1990'] + plot_help['wi_mi_il']['1990'])),
             xytext = (3, 0.5 * (plot_help['wi_mi']['1990'] + plot_help['wi_mi_il']['1990'])),
             horizontalalignment = 'center',
             verticalalignment = 'center',
             fontsize = 16)
ax1.annotate(round(plot_help['Population']['Illinois']['2000'], 1),
             xy = (4, 0.5 * (plot_help['wi_mi']['2000'] + plot_help['wi_mi_il']['2000'])),
             xytext = (4, 0.5 * (plot_help['wi_mi']['2000'] + plot_help['wi_mi_il']['2000'])),
             horizontalalignment = 'center',
             verticalalignment = 'center',
             fontsize = 16)
ax1.annotate(round(plot_help['Population']['Illinois']['2010'], 1),
             xy = (5, 0.5 * (plot_help['wi_mi']['2010'] + plot_help['wi_mi_il']['2010'])),
             xytext = (5, 0.5 * (plot_help['wi_mi']['2010'] + plot_help['wi_mi_il']['2010'])),
             horizontalalignment = 'center',
             verticalalignment = 'center',
             fontsize = 16)

# Indiana.
ax1.annotate(round(plot_help['Population']['Indiana']['1960'], 1),
             xy = (0, 0.5 * (plot_help['wi_mi_il_in']['1960'] + plot_help['wi_mi_il']['1960'])),
             xytext = (0, 0.5 * (plot_help['wi_mi_il_in']['1960'] + plot_help['wi_mi_il']['1960'])),
             horizontalalignment = 'center',
             verticalalignment = 'center',
             fontsize = 16)
ax1.annotate(round(plot_help['Population']['Indiana']['1970'], 1),
             xy = (1, 0.5 * (plot_help['wi_mi_il_in']['1970'] + plot_help['wi_mi_il']['1970'])),
             xytext = (1, 0.5 * (plot_help['wi_mi_il_in']['1970'] + plot_help['wi_mi_il']['1970'])),
             horizontalalignment = 'center',
             verticalalignment = 'center',
             fontsize = 16)
ax1.annotate(round(plot_help['Population']['Indiana']['1980'], 1),
             xy = (2, 0.5 * (plot_help['wi_mi_il_in']['1980'] + plot_help['wi_mi_il']['1980'])),
             xytext = (2, 0.5 * (plot_help['wi_mi_il_in']['1980'] + plot_help['wi_mi_il']['1980'])),
             horizontalalignment = 'center',
             verticalalignment = 'center',
             fontsize = 16)
ax1.annotate(round(plot_help['Population']['Indiana']['1990'], 1),
             xy = (3, 0.5 * (plot_help['wi_mi_il_in']['1990'] + plot_help['wi_mi_il']['1990'])),
             xytext = (3, 0.5 * (plot_help['wi_mi_il_in']['1990'] + plot_help['wi_mi_il']['1990'])),
             horizontalalignment = 'center',
             verticalalignment = 'center',
             fontsize = 16)
ax1.annotate(round(plot_help['Population']['Indiana']['2000'], 1),
             xy = (4, 0.5 * (plot_help['wi_mi_il_in']['2000'] + plot_help['wi_mi_il']['2000'])),
             xytext = (4, 0.5 * (plot_help['wi_mi_il_in']['2000'] + plot_help['wi_mi_il']['2000'])),
             horizontalalignment = 'center',
             verticalalignment = 'center',
             fontsize = 16)
ax1.annotate(round(plot_help['Population']['Indiana']['2010'], 1),
             xy = (5, 0.5 * (plot_help['wi_mi_il_in']['2010'] + plot_help['wi_mi_il']['2010'])),
             xytext = (5, 0.5 * (plot_help['wi_mi_il_in']['2010'] + plot_help['wi_mi_il']['2010'])),
             horizontalalignment = 'center',
             verticalalignment = 'center',
             fontsize = 16)

# Ohio.
ax1.annotate(round(plot_help['Population']['Ohio']['1960'], 1),
             xy = (0, 0.5 * (plot_help['wi_mi_il_in']['1960'] + plot_help['all']['1960'])),
             xytext = (0, 0.5 * (plot_help['wi_mi_il_in']['1960'] + plot_help['all']['1960'])),
             horizontalalignment = 'center',
             verticalalignment = 'center',
             fontsize = 16)
ax1.annotate(round(plot_help['Population']['Ohio']['1970'], 1),
             xy = (1, 0.5 * (plot_help['wi_mi_il_in']['1970'] + plot_help['all']['1970'])),
             xytext = (1, 0.5 * (plot_help['wi_mi_il_in']['1970'] + plot_help['all']['1970'])),
             horizontalalignment = 'center',
             verticalalignment = 'center',
             fontsize = 16)
ax1.annotate(round(plot_help['Population']['Ohio']['1980'], 1),
             xy = (2, 0.5 * (plot_help['wi_mi_il_in']['1980'] + plot_help['all']['1980'])),
             xytext = (2, 0.5 * (plot_help['wi_mi_il_in']['1980'] + plot_help['all']['1980'])),
             horizontalalignment = 'center',
             verticalalignment = 'center',
             fontsize = 16)
ax1.annotate(round(plot_help['Population']['Ohio']['1990'], 1),
             xy = (3, 0.5 * (plot_help['wi_mi_il_in']['1990'] + plot_help['all']['1990'])),
             xytext = (3, 0.5 * (plot_help['wi_mi_il_in']['1990'] + plot_help['all']['1990'])),
             horizontalalignment = 'center',
             verticalalignment = 'center',
             fontsize = 16)
ax1.annotate(round(plot_help['Population']['Ohio']['2000'], 1),
             xy = (4, 0.5 * (plot_help['wi_mi_il_in']['2000'] + plot_help['all']['2000'])),
             xytext = (4, 0.5 * (plot_help['wi_mi_il_in']['2000'] + plot_help['all']['2000'])),
             horizontalalignment = 'center',
             verticalalignment = 'center',
             fontsize = 16)
ax1.annotate(round(plot_help['Population']['Ohio']['2010'], 1),
             xy = (5, 0.5 * (plot_help['wi_mi_il_in']['2010'] + plot_help['all']['2010'])),
             xytext = (5, 0.5 * (plot_help['wi_mi_il_in']['2010'] + plot_help['all']['2010'])),
             horizontalalignment = 'center',
             verticalalignment = 'center',
             fontsize = 16)

# Set x-axis and y-axis tick label size.
plt.tick_params(axis = 'both', labelsize = 18)

# Adjust plot title spacing.
ax1.title.set_position([0.5, 1.04])

# Adjust x-axis and y-axis title spacing.
ax1.xaxis.labelpad = 8
ax1.yaxis.labelpad = 10

# Set plot and axes titles.
plt.title('Great Lakes States Population (in thousands) by Year and State',
          fontweight = 'bold',
          fontsize = 22)
plt.xlabel('Year',
           fontweight = 'bold',
           fontsize = 18)
plt.ylabel('Population (in thousands)',
           fontweight = 'bold',
           fontsize = 18)

# Add grid.
ax1.grid(zorder = 0)

# Add legend.
legend = plt.legend(title = 'State',
                    loc = 'upper left',
                    fontsize = 18,
                    bbox_to_anchor = (1.02, 0.581))
plt.setp(legend.get_title(), fontsize = 22)

# Adjust plot margins.
plt.subplots_adjust(left = 0.12,
                    bottom = 0.09,
                    right = 0.76,
                    top = 0.92)

# Show plot.
plt.show()
