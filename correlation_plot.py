# This script creates a correlation plot using 'census_data.csv'.
# A description of 'census_data.csv' can be found in 'census_data_scrape_and_process.R'.

################
# IMPORT MODULES
################
# This section imports relevant modules for the script.
import pandas as pd
from biokit.viz import corrplot

#############
# IMPORT DATA
#############
# This section imports the data that will be used in the correlation plot.

# Import data.
census_data = pd.read_csv('census_data.csv',
                          encoding = 'latin-1')
