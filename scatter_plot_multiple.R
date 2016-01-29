# This script creates two scatter plots using (subsets of) 'census_data.csv'.

# A description of 'census_data.csv' can be found in 'census_data_scrape_and_process.R'.
# The first scatter plot uses a subset of 'census_data.csv' consisting of
# all observations for 6 states (North Carolina, Maryland, New Jersey, Pennsylvania, Virginia, 
# and New York).

# The second scatter plot uses a subset of 'census_data.csv' consisiting of all observations
# for the aggregate United States row.

# Load packages.
library(data.table)
library(reshape2)
library(ggplot2)
library(Rmisc)

# Load data.
census_data = data.table(read.csv('census_data.csv', header = T, stringsAsFactors = F, check.names = F))

#####
# SUBSET/PROCESS DATA.

  # Divide population values by 1000 by easier plot viewing.
  # This command is relevant for both plots.
  census_data$`1960` = census_data$`1960` / 1000
  census_data$`1970` = census_data$`1970` / 1000
  census_data$`1980` = census_data$`1980` / 1000
  census_data$`1990` = census_data$`1990` / 1000
  census_data$`2000` = census_data$`2000` / 1000
  census_data$`2010` = census_data$`2010` / 1000

  # Create data for first scatter plot.

    # Specify states of interest.
    states = c('North Carolina', 'Maryland', 'New Jersey', 'Pennsylvania', 
               'Virginia', 'New York')
    
    # Create data subset for first scatterplot.
    census_subset_1 = census_data[Name %in% states]
    
    # Melt 'census_subset_1' to allow creation of scatter plot.
    census_subset_1 = melt(census_subset_1, id = 'Name')
    
    # Change column names of 'census_subset_1'.
    setnames(census_subset_1, names(census_subset_1), c('State', 'Year', 'Population'))
    
  # Create data for second scatter plot.
    
    # Create data subset for second scatterplot.
    census_subset_2 = census_data[Name == 'United States']
    
    # Melt 'census_subset_2' to allow creation of scatter plot.
    census_subset_2 = melt(census_subset_2, id = 'Name')
    
    # Change column names of 'census_subset_2'.
    setnames(census_subset_2, names(census_subset_2), c('Country', 'Year', 'Population'))

#####  
# PLOT DATA.
# I don't think this is a particularly good visualization, but I wanted to try having multiple plots
# in a single figure.
  
  # Create first plot.
  plot_1 = ggplot(data = census_subset_1, aes(x = Year, y = Population, color = State, shape = State)) +
            geom_point(size = 3) +
            theme(axis.text.x = element_text(color = 'black'), 
                  axis.text.y = element_text(color = 'black'), 
                  legend.position = 'bottom') +
            ylim(c(0, 20000)) +
            ggtitle('Selected State Populations (in thousands) Over Time') +
            xlab('Year') +
            ylab('Population (in thousands)')
    
  # Create second plot.
  plot_2 = ggplot(data = census_subset_2, aes(x = Year, y = Population, color = Country)) +
            geom_point(size = 3, 
                       shape = 4, 
                       colour = 'black') +
            theme(axis.text.x = element_text(color = 'black'), 
                  axis.text.y = element_text(color = 'black')) +
            ylim(c(0, 310000)) +
            ggtitle('United States Population (in thousands) Over Time') +
            xlab('Year') +
            ylab('Population (in thousands)')
  
  # Plot plots.
  multiplot(plot_1, plot_2, cols = 1)