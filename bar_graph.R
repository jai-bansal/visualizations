# This script creates a bar graph using (a subset of) 'census_data.csv'.

# A description of 'census_data.csv' can be found in 'census_data_scrape_and_process.R'.
# To avoid an overwhelming plot, I will be using a subset of 'census_data.csv' consisting of
# observations for 6 states (Delaware, Maryland, New Jersey, Pennsylvania, Virginia, 
# and West Virginia) in 2010.

# Load packages.
library(data.table)
library(ggplot2)

# Load data.
census_data = data.table(read.csv('census_data.csv', header = T, stringsAsFactors = F, check.names = F))

# SUBSET DATA.

  # Specify states of interest.
  states = c('Delaware', 'Maryland', 'New Jersey', 'Pennsylvania', 
             'Virginia', 'West Virginia')
  
  # Create data subset (specified above).
  census_subset = census_data[Name %in% states, .(Name, `2010`)]
  
  # Divided population values by 1000 for easier graph viewing.
  census_subset$`2010` = census_subset$`2010` / 1000
  
# PLOT DATA.
  
  # Set color palette.
  colors = c('#E69F00', '#56B4E9', '#009E73', '#0072B2', '#D55E00', '#CC79A7')
  
  # Plot data.
  ggplot(data = census_subset, aes(x = Name, y = `2010`, fill = colors)) + 
    geom_bar(stat = 'identity') + 
    theme(legend.position = 'none') + 
    geom_text(aes(label = round(`2010`, 1)), 
              vjust = 2) +
    ggtitle('Selected State Populations in 2010 (in thousands)') + 
    xlab('State') + 
    ylab('2010 Population (in thousands)')