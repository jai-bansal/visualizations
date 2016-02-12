# This script creates a stacked column chart using (a subset of) 'census_data.csv'.

# A description of 'census_data.csv' can be found in 'census_data_scrape_and_process.R'.
# To avoid an overwhelming plot, I will be using a subset of 'census_data.csv' consisting of
# all observations for the 'Great Lakes' region.

# This region is defined by the Bureau of Economic Analysis and can be viewed at the url below:
# https://en.wikipedia.org/wiki/List_of_regions_of_the_United_States

# The 'Great Lakes' region as defined by the Bureau of Economic Analysis contains Wisconsin, Michigan, Illinois, Indiana, and Ohio.

# Load packages.
library(data.table)
library(ggplot2)
library(reshape2)

# Load data.
census_data = data.table(read.csv('census_data.csv', 
                                  header = T, 
                                  stringsAsFactors = F, 
                                  check.names = F))

#####
# SUBSET/PROCESS DATA.

  # Remove unneeded column.
  census_data$`Area (sq. miles)` = NULL

  # Define 'Great Lakes' region.
  great_lakes = c('Wisconsin', 'Michigan', 'Illinois', 'Indiana', 'Ohio')
  
  # Subset data.
  census_subset = census_data[Name %in% great_lakes]
  
  # Divide population values by 1000 for easier graph viewing.
  census_subset$`1960` = census_subset$`1960` / 1000
  census_subset$`1970` = census_subset$`1970` / 1000
  census_subset$`1980` = census_subset$`1980` / 1000
  census_subset$`1990` = census_subset$`1990` / 1000
  census_subset$`2000` = census_subset$`2000` / 1000
  census_subset$`2010` = census_subset$`2010` / 1000

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
  
#####
# Create plot.
ggplot(data = census_subset, 
       aes(x = Year, 
           y = Population, 
           fill = State, 
           order = State)) +
    geom_bar(stat = 'identity') +
    geom_text(aes(label = round(census_subset$Population, 1), 
                  x = Year,  
                  y = y_coordinate), 
              size = 5.5, 
              color = 'white') +
    theme(axis.text.x =  element_text(color = 'black', 
                                      size = 15), 
          axis.text.y = element_text(color = 'black', 
                                     size = 15), 
          axis.title.x = element_text(face = 'bold', 
                                    size = 15, 
                                    vjust = -0.25), 
         axis.title.y = element_text(face = 'bold', 
                                    size = 15, 
                                    vjust = 1), 
         plot.title = element_text(face = 'bold',
                                  size = 17, 
                                  vjust = 2), 
         legend.title = element_text(size = 17), 
         legend.text = element_text(size = 16)) +
    ggtitle('Great Lakes Region Population (in thousands) by Year and State') +
    xlab('Year') +
    ylab('Population (in thousands)')