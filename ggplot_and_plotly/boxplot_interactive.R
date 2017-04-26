# This script creates a boxplot using 'census_data.csv' using the 'ggplot2' and 'plotly' libraries.

# A description of 'census_data.csv' can be found in 'census_data_scrape_and_process.R'.
# To avoid an overwhelming plot, I will be using a subset of 'census_data.csv' consisting of
# observations for 6 states (Delaware, Maryland, New Jersey, Pennsylvania, Virginia, 
# and West Virginia) in 2010.

# LOAD LIBRARIES ----------------------------------------------------------
# This section loads necessary libraries.
library(data.table)
library(dplyr)
library(ggplot2)
library(plotly)

# IMPORT DATA -------------------------------------------------------------
# This section imports necessary data.
# Note that the data is located in the 'visualizations' folder, NOT the 'ggplot' folder.
census_data = data.table(read.csv('census_data.csv', 
                                  header = T, 
                                  stringsAsFactors = F, 
                                  check.names = F))

# TRANSFORM DATA ------------------------------------------------------------
# This section transforms the data for plotting.

  # Remove the rows for the entire United States, a few states the skew the results, and the column 'Area (sq. miles)'.
  census_data = census_data[!(Name %in% c('United States', 'California', 'New York', 'Texas', 'Florida'))]
  census_data = select(census_data, 
                       -c(`Area (sq. miles)`))

  # Melt 'census_data'.
  melted_data = melt(census_data, 
                     id.vars = c('Name'))
  
# PLOT DATA ---------------------------------------------------------------
# This section plots the data.
ggplotly(ggplot(data = melted_data, 
                aes(x = variable, 
                    y = value, 
                    color = variable)) +
           geom_boxplot() + 
           theme(legend.position = 'none') + 
           labs(x = 'Year', 
                y = 'Population', 
                title = 'Population Distribution by Year'))

