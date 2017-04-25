# This script creates a pie chart using (a subset of) 'census_data.csv' using the 'rCharts' library.

# A description of 'census_data.csv' can be found in 'census_data_scrape_and_process.R'.
# To avoid an overwhelming plot, I will be using a subset of 'census_data.csv' consisting of
# observations for 6 states (North Carolina, Maryland, New Jersey, Pennsylvania, Virginia, 
# and New York) in 2010.

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

  # Specify states of interest.
  states = c('North Carolina', 'Maryland', 'New Jersey', 'Pennsylvania', 
             'Virginia', 'New York')
  
  # Create data subset (specified above).
  census_subset = census_data[Name %in% states, .(Name, `2010`)]
  
  # Divide population values by 1000000 for easier graph viewing.
  census_subset$`2010` = census_subset$`2010` / 1000000
  
  # Compute percentage of total population accounted for by each state.
  
    # Compute percentage.
    census_subset$percent = round(100 * (census_subset$`2010` / sum(census_subset$`2010`)), 2)

  # Specify locations for pie chart labels.
  
    # Count cumulative population.
    # This has no statistical or data significance, it's only to help with chart labels.
    census_subset$sum = cumsum(census_subset$`2010`)
    
    # Create 'offset_sum' column that will help with chart labels.
    census_subset$offset_sum = c(0, census_subset$sum[1:(nrow(census_subset) - 1)])
    
    # Create 'label_locations' column that specifies label locations on pie chart.
    census_subset$label_locations = (census_subset$sum + census_subset$offset_sum) / 2

# PLOT DATA ---------------------------------------------------------------
# This section plots the data.
nPlot(x = 'Name', 
      y = 'percent', 
      data = census_subset, 
      type = 'pieChart')
