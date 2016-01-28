# This script creates a motion chart using (a subset of) 'census_data.csv'.

# A description of 'census_data.csv' can be found in 'census_data_scrape_and_process.R'.
# To avoid an overwhelming plot, I will be using a subset of 'census_data.csv' consisting of
# all observations for the  'Far West' and 'Southwest' regions.

# These regions are defined by the Bureau of Economic Analysis and can be viewed at the url below:
# https://en.wikipedia.org/wiki/List_of_regions_of_the_United_States

# The 'Far West' region consists of Washington, Oregon, California, and Nevada.
# The 'Southwest' region consists of Arizona, New Mexico, Texas, and Oklahoma.

# Load packages.
library(data.table)
library(reshape2)
library(googleVis)

# Load data.
census_data = data.table(read.csv('census_data.csv', header = T, stringsAsFactors = F, check.names = F))

#####
# SUBSET/PROCESS DATA.

  # Define regions.
  far_west = c('Washington', 'Oregon', 'California', 'Nevada')
  southwest = c('Arizona', 'New Mexico', 'Texas', 'Oklahoma')
  
  # Subset data.
  census_subset = census_data[(Name %in% far_west) | (Name %in% southwest)]

  # Melt 'census_subset' to allow motion chart.
  census_subset = melt(census_subset, id = 'Name')
  
  # Add 'Region' column to 'census_subset'.
  census_subset$Region = ifelse(census_subset$Name %in% far_west, 'Far West', 'Southwest')

  # Rename columns of 'census_data'.
  setnames(census_subset, names(census_subset), c('State', 'Year', 'Population', 'Region'))
  
  # Change 'census_data$Year' to 'numeric' type.
  census_subset$Year = as.numeric(as.character(census_subset$Year))
  
#####
# Create motion chart.
fig = gvisMotionChart(data = census_subset, idvar = 'State', timevar = 'Year', xvar = 'Region', yvar = 'Population')
plot(fig)