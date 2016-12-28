# This script creates a correlation plot using (a subset of) 'census_data.csv'.
# A description of 'census_data.csv' can be found in 'census_data_scrape_and_process.R'.

# LOAD LIBRARIES ----------------------------------------------------------
# This section loads relevant libraries.
library(readr)
library(data.table)
library(dplyr)
library(corrplot)

# IMPORT DATA -------------------------------------------------------------
# This section imports the data to be used in the correlation plot.
census_data = data.table(read_csv('census_data.csv'))

# CLEAN DATA --------------------------------------------------------------
# This section cleans the data so the correlation plot shows up properly.

  # Remove 'Name' from 'census_data'.
  # All correlation plot data must be numeric.
  census_data = select(census_data, 
                       -c(Name))

  # Remove null values from 'Area (sq. miles)'.
  correlation_plot_data = census_data[is.na(`Area (sq. miles)`) == F]
  

# ADD FEATURE -------------------------------------------------------------
# This section adds features to 'correlation_plot_data' that are negatively correlated with each other.
# This results in the correlation plot showing an example of how negative correlations look.
  
  # Add population growth in percentage terms between 1960 and 1970.
  correlation_plot_data$`60_70_percent_growth` = (correlation_plot_data$`1970` - correlation_plot_data$`1960`) / correlation_plot_data$`1960`

  # Add population growth in percentage terms between 1970 and 1980.
  correlation_plot_data$`70_80_percent_growth` = (correlation_plot_data$`1980` - correlation_plot_data$`1970`) / correlation_plot_data$`1970`
  
# CREATE CORRELATION PLOT -------------------------------------------------
# This section creates a correlation plot (using only numeric columns).
corrplot(cor(correlation_plot_data))

