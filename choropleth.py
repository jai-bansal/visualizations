# This script creates a choropleth map using (a subset of) 'census_data.csv'.

# A description of 'census_data.csv' can be found in 'census_data_scrape_and_process.R'.
# To avoid an overwhelming plot, I will be using a subset of 'census_data.csv' consisting of
# all observations for the year 2010.

# Import modules.
import pandas as pd
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from matplotlib import style

# Set style.
style.use('seaborn-talk')

# Load data.
census_data = pd.read_csv('census_data.csv', encoding = 'latin-1')

# SUBSET/PROCESS DATA.

# Restrict 'census_subset' to '2010' observations only.
census_subset = census_data[['Name', '2010']]

# Remove aggregate 'United States' population row.
census_subset = census_subset[census_subset['Name'] != 'United States']

# Divide '2010' population value by 1000 for easier graph viewing.
census_subset['2010'] = census_subset['2010'] / 1000

# PLOT DATA.

# Create map.
# Lambert Conformal map of lower 48 states.
m = Basemap(llcrnrlon=-119,llcrnrlat=22,urcrnrlon=-64,urcrnrlat=49,
            projection='lcc',lat_1=33,lat_2=45,lon_0=-95)
# draw state boundaries.
# data from U.S Census Bureau
# http://www.census.gov/geo/www/cob/st2000.html
shp_info = m.readshapefile('st99_d00','states',drawbounds=True)

#m.drawstates()

# Set plot titles.
plt.title('2010 Contiguous United States Population (in thousands) by State', fontweight = 'bold')

# Adjust plot margins.
# plt.subplots_adjust(left = 0.25, bottom = 0.22, right = 0.67, top = 0.95)

# Show plot.
plt.show()
