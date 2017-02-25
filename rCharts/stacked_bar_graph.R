# This script creates a stacked bar chart using (a subset of) 'census_data.csv' using the 'rCharts' library.

# A description of 'census_data.csv' can be found in 'census_data_scrape_and_process.R'.
# To avoid an overwhelming plot, I will be using a subset of 'census_data.csv' consisting of
# all observations for the 'Great Lakes' region.

# This region is defined by the Bureau of Economic Analysis and can be viewed at the url below:
# https://en.wikipedia.org/wiki/List_of_regions_of_the_United_States

# The 'Great Lakes' region as defined by the Bureau of Economic Analysis contains Wisconsin, Michigan, Illinois, Indiana, and Ohio.

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

  # Define 'Great Lakes' region.
  great_lakes = c('Wisconsin', 'Michigan', 'Illinois', 'Indiana', 'Ohio')
  
  # Subset data.
  census_subset = census_data[Name %in% great_lakes]
  
  # Divide population values by 1000000 for easier graph viewing.
  census_subset$`1960` = census_subset$`1960` / 1000000
  census_subset$`1970` = census_subset$`1970` / 1000000
  census_subset$`1980` = census_subset$`1980` / 1000000
  census_subset$`1990` = census_subset$`1990` / 1000000
  census_subset$`2000` = census_subset$`2000` / 1000000
  census_subset$`2010` = census_subset$`2010` / 1000000

  # Melt 'census_subset' to allow stacked bar graph.
  census_subset = melt(census_subset, 
                       id = 'Name')
  
  # Rename columns of 'census_data'.
  setnames(census_subset, 
           names(census_subset), 
           c('State', 'Year', 'Population'))
  
  # Specify y-coordinates for label positions.
    
    # Sort 'census_subset' by  'Year' and then 'State'.
    # This puts the 'State' data for each year in the same order as it will be plotted in.
    census_subset = census_subset[order(Year, State)]
    
    # Keep track of cumulative population by 'Year'.
    census_subset[, sum := cumsum(Population), by = 'Year']
    
    # Create 'y_coordinate' column for each observation's label.
    census_subset$y_coordinate = ((2 * census_subset$sum) - census_subset$Population) / 2
  
# PLOT DATA ---------------------------------------------------------------
# This section plots the data.
stacked_bar_chart= nPlot(Population ~ Year, 
                         group = 'State', 
                         type = 'multiBarChart', 
                         data = census_subset)
stacked_bar_chart$xAxis(axisLabel = 'Year')
stacked_bar_chart