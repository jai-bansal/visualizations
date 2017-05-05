# This script creates an interactive bar graph using 'census_data.csv'.

# A description of 'census_data.csv' can be found in 'census_data_scrape_and_process.R'.

################
# IMPORT MODULES
################

# Import modules.
import pandas as pd
import numpy as np
import plotly.plotly as py
import plotly.graph_objs as go

#############
# IMPORT DATA
#############
# Note that the data is located in the 'visualizations' folder.

# Load data.
census_data = pd.read_csv('census_data.csv',
                          encoding = 'latin-1')

################
# TRANSFORM DATA
################


