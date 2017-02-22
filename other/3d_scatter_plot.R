# This script creates a 3 dimensional scatter plot using (a subset of) 'census_data.csv'.

# A description of 'census_data.csv' can be found in 'census_data_scrape_and_process.R'.
# To avoid an overwhelming plot, I will be using a subset of 'census_data.csv' consisting of
# observations for 4 states (Maryland, Pennsylvania, Virginia, and West Virginia) in 2010.

# Load packages.
library(data.table)
library(reshape2)
library(scatterplot3d)

# Load data.
# Note that the data is located in the 'visualizations' folder, NOT the 'ggplot' folder.
census_data = data.table(read.csv('census_data.csv', 
                                  header = T, 
                                  stringsAsFactors = F, 
                                  check.names = F))

#####
# SUBSET/PROCESS DATA.

  # Specify states of interest.
  states = c('Maryland', 'Pennsylvania', 'Virginia', 'West Virginia')

  # Subset data.
  census_subset = census_data[Name %in% states]

  # Divide population values by 1000000 for easier graph viewing.
  census_subset$`1960` = census_subset$`1960` / 1000000
  census_subset$`1970` = census_subset$`1970` / 1000000
  census_subset$`1980` = census_subset$`1980` / 1000000
  census_subset$`1990` = census_subset$`1990` / 1000000
  census_subset$`2000` = census_subset$`2000` / 1000000
  census_subset$`2010` = census_subset$`2010` / 1000000
  
  # Divide area values by 1000 for easier graph viewing.
  census_subset$`Area (sq. miles)` = census_subset$`Area (sq. miles)` / 1000
  
  # Keep state areas in separate data frame and rename columns.
  areas = census_subset[, .(Name, `Area (sq. miles)`)]
  setnames(areas, 
           names(areas), 
           c('State', 'Area (sq. miles)'))
  
  # Remove 'Area (sq. miles) from 'census_subset' to allow melt.
  census_subset$`Area (sq. miles)` = NULL
    
  # Melt 'census_subset' to allow 3 dimensional plot and rename columns.
  census_subset = melt(census_subset, 
                       id = 'Name')
  setnames(census_subset, 
           names(census_subset), 
           c('State', 'Year', 'Population'))
  
  # Add 'areas' to 'census_subset'.
  census_subset = merge(census_subset, 
                        areas, 
                        by = 'State')
  
  # Change 'census_subset$Year' to character vector.
  census_subset$Year = as.character(census_subset$Year)
  
  # Add 'colors' column.
  # Each state gets a color which will be that state's color in the plot.
  census_subset$colors = ifelse(census_subset$State == 'Maryland', 'blue', 
                                ifelse(census_subset$State == 'Pennsylvania', 'red', 
                                       ifelse(census_subset$State == 'Virginia', 'green', 'orange')))
  
  # Add a 'shape_number' column.
  # Each state gets a number which will correspond to that state's shape in the plot.
  census_subset$shape_number = ifelse(census_subset$State == 'Maryland', 15, 
                                      ifelse(census_subset$State == 'Pennsylvania', 16, 
                                             ifelse(census_subset$State == 'Virginia', 17, 18)))

#####
# PLOT DATA.
  
  # Create scatter plot.
  scatterplot3d(x = census_subset$Year,
    y = census_subset$Population,     
    z = census_subset$`Area (sq. miles)`,
    color = census_subset$colors,
    pch = census_subset$shape_number, 
    type = 'h',
    angle = 290,
    main = 'Selected State Populations and Areas Over Time', 
    xlab = 'Year', 
    ylab = 'Population (in millions)', 
    zlab = 'Area (thousands of sq. miles)')
  
  # Add legend.
  legend('bottom', 
         legend = levels(as.factor(census_subset$State)), 
         col =  c('blue', 'red', 'green', 'orange'), 
         pch = c(15, 16, 17, 18), 
         horiz = T,
         xpd = T,
         inset = -0.35)