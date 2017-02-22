# This script creates a scatter plot using (a subset of) 'census_data.csv'.

# A description of 'census_data.csv' can be found in 'census_data_scrape_and_process.R'.
# To avoid an overwhelming plot, I will be using a subset of 'census_data.csv' consisting of
# all observations for 6 states (North Carolina, Maryland, New Jersey, Pennsylvania, Virginia, 
# and New York).

# Load packages.
library(data.table)
library(reshape2)
library(ggplot2)

# Load data.
# Note that the data is located in the 'visualizations' folder, NOT the 'ggplot' folder.
census_data = data.table(read.csv('census_data.csv', 
                                  header = T, 
                                  stringsAsFactors = F, 
                                  check.names = F))

#####
# SUBSET/PROCESS DATA.

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

#####  
# Plot data.
ggplot(data = census_subset, 
       aes(x = Year, 
           y = Population, 
           color = State, 
           shape = State)) +
  geom_point(size = 4) +
  scale_y_continuous(breaks = seq(2.5, 20, by = 2.5)) +
  theme(axis.text.x = element_text(color = 'black', 
                                   size = 17), 
        axis.text.y = element_text(color = 'black', 
                                   size = 17), 
        axis.title.x = element_text(face = 'bold', 
                                    size = 17, 
                                    vjust = -0.25), 
        axis.title.y = element_text(face = 'bold', 
                                    size = 17, 
                                    vjust = 1), 
        plot.title = element_text(face = 'bold',
                                  size = 19, 
                                  vjust = 1.5), 
        legend.title = element_text(size = 19), 
        legend.text = element_text(size = 18)) +
  ggtitle('Selected State Populations (in millions) Over Time') +
  xlab('Year') +
  ylab('Population (in millions)')