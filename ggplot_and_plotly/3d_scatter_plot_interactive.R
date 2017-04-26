# This script creates a 3 dimensional scatter plot using (a subset of) 'census_data.csv'.

# A description of 'census_data.csv' can be found in 'census_data_scrape_and_process.R'.

# Load packages.
library(data.table)
library(plotly)

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

  # Create plot.
  plot_ly(data = census_subset, 
          x = ~Population, 
          y = ~Year, 
          z = ~`Area (sq. miles)`, 
          color = ~State, 
          colors = c('#ff0000', '#0066ff', '#339933', '#ff9900'), 
          type = 'scatter3d', 
          mode = 'lines+markers', 
          hoverinfo = 'text', 
          text = ~paste0('Population: ', 
                         round(census_subset$Population, 1), 
                         'M', 
                         '<br>', 
                         'Year: ', 
                         census_subset$Year, 
                         '<br>', 
                         'Area: ',
                         round(census_subset$`Area (sq. miles)`, 1), 
                         ' thousand sq. miles')) %>% 
      layout(title = 'Selected State Populations and Areas Over Time', 
             scene = list(xaxis = list(title = 'Pop. (millions)'), 
                          yaxis = list(title = 'Year'), 
                          zaxis = list(title = 'Area (1000s of sq. miles)')))
