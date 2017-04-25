# This script creates a scatter plot using (a subset of) 'census_data.csv' using the 'rCharts' library.

# A description of 'census_data.csv' can be found in 'census_data_scrape_and_process.R'.
# To avoid an overwhelming plot, I will be using a subset of 'census_data.csv' consisting of
# all observations for 6 states (North Carolina, Maryland, New Jersey, Pennsylvania, Virginia, 
# and New York).

# LOAD LIBRARIES ----------------------------------------------------------
# This section loads the necessary libraries for this script.
library(readr)
library(data.table)
library(rCharts)

# IMPORT DATA -------------------------------------------------------------
# This section imports the data for this script.
# Note that the data is in the 'visualizations' folder, NOT the 'rCharts' folder.
census_data = data.table(read_csv('census_data.csv'))

# SUBSET/PROCESS DATA -----------------------------------------------------
# This section prepares the data prior to plotting.

  # Remove unneeded column.
  census_data$`Area (sq. miles)` = NULL

  # Specify states of interest.
  states = c('North Carolina', 'Maryland', 'New Jersey', 'Pennsylvania', 
             'Virginia', 'New York')
  
  # Create data subset (specified above).
  census_subset = census_data[Name %in% states]
  
  # Divided population values by 1000000 for easier graph viewing.
  census_subset$`1960` = census_subset$`1960` / 1000000
  census_subset$`1970` = census_subset$`1970` / 1000000
  census_subset$`1980` = census_subset$`1980` / 1000000
  census_subset$`1990` = census_subset$`1990` / 1000000
  census_subset$`2000` = census_subset$`2000` / 1000000
  census_subset$`2010` = census_subset$`2010` / 1000000
  
  # Melt 'census_subset' to allow creation of scatter plot.
  census_subset = melt(census_subset, 
                       id = 'Name')
  
  # Change column names of 'census_subset'.
  setnames(census_subset, 
           names(census_subset), 
           c('State', 'Year', 'Population'))

# PLOT DATA ---------------------------------------------------------------
# This section plots the data.
rPlot(Population ~ Year, 
      data = census_subset, 
      type = 'point', 
      color = 'State')