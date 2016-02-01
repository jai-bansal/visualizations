# This script creates a line graph using (a subset of) 'census_data.csv'.

# A description of 'census_data.csv' can be found in 'census_data_scrape_and_process.R'.
# To avoid an overwhelming plot, I will be using a subset of 'census_data.csv' consisting of
# all observations for Pennsylvania and Illinois.

# Import modules.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load data.
census_data = pd.read_csv('census_data.csv', encoding = 'latin-1')

# SUBSET/PROCESS DATA.
